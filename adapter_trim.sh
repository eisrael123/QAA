#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --cpus-per-task=16                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB per cpu
#SBATCH --nodes=1
#SBATCH --output=output_%j.log   # STDOUT
#SBATCH --error=error_%j.log     # STDERR
#SBATCH --mail-user=ewi@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email 
set -e 

f1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/3.1Gb_SAMN36981042_1.fastq.gz"
f2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/3.2Gb_SAMN36981042_2.fastq.gz"
f3="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/3.1Gb_SAMN36982003_1.fastq.gz"
f4="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/3.1Gb_SAMN36982003_2.fastq.gz"

out1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r1_ADAPTER_REMOVED.fastq.gz"
out2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r2_ADAPTER_REMOVED.fastq.gz"
out3="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r1_ADAPTER_REMOVED.fastq.gz"
out4="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r2_ADAPTER_REMOVED.fastq.gz"

R1adapter="AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"
R2adapter="AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"

echo "trimmer #1 is running."
/usr/bin/time -v cutadapt -a $R1adapter -A $R2adapter -o $out1 -p $out2 $f1 $f2
echo "trimmer #1 is complete."

echo "trimmer #2 is running."
/usr/bin/time -v cutadapt -a $R1adapter -A $R2adapter -o $out3 -p $out4 $f3 $f4
echo "trimmer #2 is complete."

