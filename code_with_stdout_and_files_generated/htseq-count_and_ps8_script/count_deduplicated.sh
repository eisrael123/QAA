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

#analyze with PS8 script
sam_out="sam_analyzer_output.txt"
in1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/deduplicated_results_rhy49/deduplicated.sam"
in2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/deduplicated_results_rhy106/deduplicated.sam"
# /usr/bin/time -v ./sam_analyzer.py -f $in1 > $sam_out
# /usr/bin/time -v ./sam_analyzer.py -f $in2 >> $sam_out


#analyze with htseq-count
features="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/campylomormyrus.gff"

o1="rhy_49_counts_yes.txt"
o2="rhy_49_counts_reverse.txt"
/usr/bin/time -v htseq-count --stranded=yes --idattr=ID $in1 $features > $o1
/usr/bin/time -v htseq-count --stranded=reverse --idattr=ID $in1 $features > $o2

o1="rhy_106_counts_yes.txt"
o2="rhy_106_counts_reverse.txt"
/usr/bin/time -v htseq-count --stranded=yes --idattr=ID $in2 $features > $o1
/usr/bin/time -v htseq-count --stranded=reverse --idattr=ID $in2 $features > $o2
exit 