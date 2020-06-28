import sys, os

def prtVer():
		print '''    ###  qg09 python version  ###
     Version  :  0.0(alpha)
     Developer:  Xin Chen
     Data     :  2017/10/11  '''

def wrtScript(ncore,jobname,node):
	Inputfile = open('qg09.pbs','w')
	lines1 = '''#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -N Gauss09
#$ -V
'''
	linesCores = "#$ -pe  linda " + str(ncore) + "\n"
	lineNode = "#$ -l h=" +node+ "\n"
	lineName = "jobname=" +jobname +"\n"
	lines2 = '''username=`whoami`
GAUSS_RUNDIR=/tmp/${username}.$JOB_ID
if [ ! -a $GAUSS_RUNDIR ]; then
mkdir -p $GAUSS_RUNDIR
fi
export GAUSS_RUNDIR
GAUSS_SCRDIR=/tmp/${username}.$JOB_ID/${jobname}
if [ ! -a $GAUSS_SCRDIR ]; then
   mkdir -p $GAUSS_SCRDIR
   fi
export GAUSS_SCRDIR
cp $SGE_O_WORKDIR/${jobname}.* $GAUSS_RUNDIR
cd $GAUSS_RUNDIR
time g09 $jobname
mv $GAUSS_RUNDIR/${jobname}.* $SGE_O_WORKDIR
mv $GAUSS_RUNDIR/*.chk $SGE_O_WORKDIR
rm -rf $GAUSS_RUNDIR
rm -rf $SGE_O_WORKDIR/$REQUEST.e*
rm -rf $SGE_O_WORKDIR/$REQUEST.o*
rm -rf $SGE_O_WORKDIR/$REQUEST.p*
'''
	Inputfile.writelines(lines1)
	Inputfile.writelines(linesCores)
	Inputfile.writelines(lineName)
	Inputfile.writelines(lines2)
def prtHelp():
		print '''
       ##########################################
       #    qg09.py help file                   #
       #                                        #
       #                                        #
       ##########################################
       Options include:
             qg09.py --version    : Prints the version number
             qg09.py --help       : Display this help
             qg09.py -i NAME      : Submit a Gaussian job
             qg09.py -p cores     : CPU core Number (Default 8)
             qg09.py -h nodeName  : Specify submit jobs to which nodes(cu01,cu02,...cu201). 

              (Sequence doesn't matter)
       Examples:
       1) Submit a file named job.gjf using 16 cores
              qg09.py -i job.gjf -p 16
       2) Submit a file named job.gjf using 16 cores to cu01 node
              qg09.py -i job.gjf -p 16 -h cu01
			 ''' 


if __name__ == '__main__':

	if sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option == 'version':
			prtVer()
		elif option == 'help':
			prtHelp()
	ncore = 8
	node = ''
	jobname = ''
	for i in range(1,len(sys.argv)-1):
		if sys.argv[i] == '-p':
			ncore = int( sys.argv[i+1])

		if sys.argv[i] == '-h':
			node  = sys.argv[i+1]
				
		if sys.argv[i] == '-i':
			jobname = sys.argv[i+1]
	if len(jobname) == 0 :
		print "Null job name ! Exit"
		sys.exit()

	print "Ncores   :",ncore
	print "jobname  :",jobname 
	print "Nodename :",node
# Write batch script
	wrtScript(ncore,jobname,node)
# Commit jobs

