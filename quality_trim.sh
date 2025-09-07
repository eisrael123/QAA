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

f1="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r1_ADAPTER_REMOVED.fastq.gz"
f2="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r2_ADAPTER_REMOVED.fastq.gz"
f3="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r1_ADAPTER_REMOVED.fastq.gz"
f4="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r2_ADAPTER_REMOVED.fastq.gz"

out1_paired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r1_ADAPTER_REMOVED_paired.fastq.gz"
out1_unpaired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r1_ADAPTER_REMOVED_unpaired.fastq.gz"
out2_paired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r2_ADAPTER_REMOVED_paired.fastq.gz"
out2_unpaired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r2_ADAPTER_REMOVED_unpaired.fastq.gz"
out3_paired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r1_ADAPTER_REMOVED_paired.fastq.gz"
out3_unpaired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r1_ADAPTER_REMOVED_unpaired.fastq.gz"
out4_paired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r2_ADAPTER_REMOVED_paired.fastq.gz"
out4_unpaired="/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r2_ADAPTER_REMOVED_unpaired.fastq.gz"


trimmomaticjarfile="/home/ewi/miniforge3/envs/QAA/share/trimmomatic-0.40-0/trimmomatic.jar"

# echo "trimmer #1 is running."
# /usr/bin/time -v java -jar $trimmomaticjarfile PE -phred33 $f1 $f2 $out1_paired $out1_unpaired $out2_paired $out2_unpaired LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35
# echo "trimmer #1 is complete."

echo "trimmer #2 is running."
/usr/bin/time -v java -jar $trimmomaticjarfile PE -phred33 $f3 $f4 $out3_paired $out3unpaired $out4_paired $out4_unpaired LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35
echo "trimmer #2 is complete."
