import sys, os

def prtVer():
		print '''    ###  qg09 python version  ###
     Version  :  0.0(alpha)
     Developer:  Xin Chen
     Data     :  2017/10/11  '''
	

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
             qg09.py -v           : Check Gaussian version
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
	print sys.argv
