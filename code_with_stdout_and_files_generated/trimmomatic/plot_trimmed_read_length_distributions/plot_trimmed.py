#!/usr/bin/env python 
import matplotlib.pyplot as plt
import gzip 
import numpy as np

def dict_to_data_list(d):
    """Converts the length:counts dictionary to a list of raw data points."""
    data = []
    for value, frequency in d.items():
        data.extend([value] * frequency)
    return np.array(data)

# TO INITIALIZE DATA

fileR1 = "/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r1_ADAPTER_REMOVED_paired.fastq.gz"
fileR2 = "/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy49_electric_organ_adult/r2_ADAPTER_REMOVED_paired.fastq.gz"
fileR3 = "/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r1_ADAPTER_REMOVED_paired.fastq.gz"
fileR4 = "/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/Campylomormyrus_rhynchophorus_rhy106_electric_organ_adult/r2_ADAPTER_REMOVED_paired.fastq.gz"

dist_rhy49_R1 = {i: 0 for i in range(151)} #max length
dist_rhy49_R2 = {i: 0 for i in range(151)}
dist_rhy106_R1 = {i: 0 for i in range(151)}
dist_rhy106_R2 = {i: 0 for i in range(151)}
with (
    gzip.open(fileR1,"rt") as r1, 
    gzip.open(fileR2,"rt") as r2, 
    gzip.open(fileR3,"rt") as r3, 
    gzip.open(fileR4,"rt") as r4, 
):
    index = 1
    while True:     
        read1 = r1.readline().strip()
        read2 = r2.readline().strip()
        if read1 == '' or read2 == '':
            break
        if index%4 == 2:
            dist_rhy49_R1[len(read1)] += 1
            dist_rhy49_R2[len(read2)] += 1
        index += 1
    
    index = 1
    while True:     
        read1 = r3.readline().strip()
        read2 = r4.readline().strip()
        if read1 == '' or read2 == '':
            break
        if index%4 == 2:
            dist_rhy106_R1[len(read1)] += 1
            dist_rhy106_R2[len(read2)] += 1
        index += 1

with open("trimmed_distributions.txt", 'w') as f:
    f.write(f"{dist_rhy49_R1}\n{dist_rhy49_R2}\n{dist_rhy106_R1}\n{dist_rhy106_R2}")

## TO RETRIEVE DATA
# with open('/projects/bgmp/ewi/bioinfo/Bi623/Assignments/QAA/trimmed_distributions.txt', 'r') as f:
#     dist_rhy49_R1 = eval(f.readline().strip())
#     dist_rhy49_R2 = eval(f.readline().strip())
#     dist_rhy106_R1 = eval(f.readline().strip())
#     dist_rhy106_R2 = eval(f.readline().strip())


#convert dictionary to data list
data1 = dict_to_data_list(dist_rhy49_R1)
data2 = dict_to_data_list(dist_rhy49_R2)

#plot data
plt.figure(figsize=(10, 6))
plt.hist(data1, bins=len(dist_rhy49_R1.keys()), label='Read 1', alpha=0.6)
plt.hist(data2, bins=len(dist_rhy49_R1.keys()), label='Read 2', alpha=0.6)
plt.title('Histogram from Frequency Dictionary', fontsize=16)
plt.title('Histograms of Read 1 and Read 2 for Rhy49', fontsize=16)
plt.xlabel('Length', fontsize=12)
plt.xticks(np.arange(min(min(data1),min(data2)), max(max(data1),max(data2)), 10))
plt.ylabel('Frequency', fontsize=12)
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.savefig('combined_histograms_rhy49.png')
plt.close()

data1 = dict_to_data_list(dist_rhy106_R1)
data2 = dict_to_data_list(dist_rhy106_R2)
plt.figure(figsize=(10, 6))
plt.hist(data1, bins=len(dist_rhy106_R1.keys()), label='Read 1', alpha=0.6)
plt.hist(data2, bins=len(dist_rhy106_R1.keys()), label='Read 2', alpha=0.6)
plt.title('Histogram from Frequency Dictionary', fontsize=16)
plt.title('Histograms of Read 1 and Read 2 for Rhy106', fontsize=16)
plt.xlabel('Length', fontsize=12)
plt.xticks(np.arange(min(min(data1),min(data2)), max(max(data1),max(data2)), 10))
plt.ylabel('Frequency', fontsize=12)
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.savefig('combined_histograms_rhy106.png')
plt.close()



