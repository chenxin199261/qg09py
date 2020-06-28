# qg09py

A python script to submit gaussian09 job to server.

This program generates a pbs file


<code>

#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -N Gauss09
#$ -pe  linda 8
#$ -V
jobname=CAStest
username=`whoami`
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
time g09 $jobname.com
mv $GAUSS_RUNDIR/${jobname}.* $SGE_O_WORKDIR
mv $GAUSS_RUNDIR/*.chk $SGE_O_WORKDIR
rm -rf $GAUSS_RUNDIR
rm -rf $SGE_O_WORKDIR/$REQUEST.e*
rm -rf $SGE_O_WORKDIR/$REQUEST.o*
rm -rf $SGE_O_WORKDIR/$REQUEST.p*


</code>
       
       
# Examples:
       1) Submit a file named job.gjf using 16 cores
              qg09.py -i job.gjf -p 16
       2) Submit a file named job.gjf using 16 cores to cu01 node
              qg09.py -i job.gjf -p 16 -h cu01
