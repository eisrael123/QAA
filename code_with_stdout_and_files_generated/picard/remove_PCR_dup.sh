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

f1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/align_results_rhy49/Aligned.out.sam"
o1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/align_results_rhy49/Aligned.out.SORTED.sam"

f2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/align_results_rhy106/Aligned.out.sam"
o2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/align_results_rhy106/Aligned.out.SORTED.sam"


echo "sorting SAM for rhy46"
samtools sort -O SAM -o $o1 $f1
echo "done"

echo "sorting SAM for rhy106"
samtools sort -O SAM -o $o2 $f2
echo "done"

pcr_out1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/align_results_rhy49/deduplicated.sam"
pcr_out2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/align_results_rhy106/deduplicated.sam"

echo "Removing PCR dups for rhy49 R1"
/usr/bin/time -v picard MarkDuplicates I=$o1 O=$pcr_out1 M=metrics_rhy49.txt.metrics REMOVE_DUPLICATES=TRUE VALIDATION_STRINGENCY=LENIENT
echo "done"

echo "Removing PCR dups for rhy106 R2"
/usr/bin/time -v picard MarkDuplicates I=$o2 O=$pcr_out2 M=metrics_rhy106.txt.metrics REMOVE_DUPLICATES=TRUE VALIDATION_STRINGENCY=LENIENT
echo "done"
exit 