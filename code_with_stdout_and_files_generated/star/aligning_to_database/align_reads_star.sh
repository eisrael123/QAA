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

f1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r1_ADAPTER_REMOVED_paired.fastq.gz"
f2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r2_ADAPTER_REMOVED_paired.fastq.gz"
f3="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r1_ADAPTER_REMOVED_paired.fastq.gz"
f4="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r2_ADAPTER_REMOVED_paired.fastq.gz"
o1="align_results_rhy49/"
o2="align_results_rhy106/"
dir="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_compressirostris.STAR_2.7.11b"

echo "first star alignment for rhy46 running"
/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn $f1 $f2 \
--genomeDir $dir \
--outFileNamePrefix $o1
echo "done"

echo "second star alignment for rhy106 running"
/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn $f3 $f4 \
--genomeDir $dir \
--outFileNamePrefix $o2
echo "done"
exit 