#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH --nodes=1
#SBATCH --output=output_%j.log   # STDOUT
#SBATCH --error=error_%j.log     # STDERR
#SBATCH --mail-user=ewi@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email 
set -e

#first output recommended a preindexing string of 13, so added option --genomeSAindexNbases 13
/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate --genomeSAindexNbases 13 --genomeDir Campylomormyrus_compressirostris.STAR_2.7.11b --genomeFastaFiles /projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/campylomormyrus.fasta --sjdbGTFfile /projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/campylomormyrus.gtf
echo "done"
exit 