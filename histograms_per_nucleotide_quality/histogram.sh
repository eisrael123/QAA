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

echo "histogram generator p1 is running."
/usr/bin/time -v ./histogram_generator_part1.py $f1 $f2 $f3 $f4 > processed_data_p1.txt
echo "histogram generator p1 is complete."

echo "histogram generator p2 is running."
/usr/bin/time -v ./histogram_generator_part2.py processed_data_p1.txt
echo "histogram generator p2 is complete."
