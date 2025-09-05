#!/usr/bin/env python 
import bioinfo  
import matplotlib.pyplot as plt
import os
import sys
import gzip 
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Process input files and writes data for per nucleotide quality averages.")
    parser.add_argument('file1', type=str, help='The path to the first file.')
    parser.add_argument('file2', type=str, help='The path to the second file.')
    parser.add_argument('file3', type=str, help='The path to the third file.')
    parser.add_argument('file4', type=str, help='The path to the fourth file.')
    return parser.parse_args()

#parameters
args = get_args()

fileR1 = args.file1
fileR2 = args.file2
fileR3 = args.file3
fileR4 = args.file4


dist_r1 = {i:[0,0] for i in range(150)}
dist_r2 = {i:[0,0] for i in range(150)}
dist_r3 = {i:[0,0] for i in range(150)}
dist_r4 = {i:[0,0] for i in range(150)}
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
        if index%4 == 0:
            for j in range(len(read1)):
                qual_score_r1 = bioinfo.convert_phred(read1[j]) 
                sum, counts = dist_r1.get(j,[0, 0])
                dist_r1[j] = [sum + qual_score_r1, counts + 1]
            for j in range(len(read2)):
                qual_score_r2 = bioinfo.convert_phred(read2[j])
                sum, counts = dist_r2.get(j,[0, 0])
                dist_r2[j] = [sum + qual_score_r2, counts + 1]
        index += 1
    print(f"{dist_r1}")
    print(f"{dist_r2}")

    index = 1
    while True:     
        read3 = r3.readline().strip()
        read4 = r4.readline().strip()
        if read3 == '' or read4 == '':
            break
        if index%4 == 0:
            for j in range(len(read3)):
                qual_score_r3 = bioinfo.convert_phred(read3[j]) 
                sum, counts = dist_r3.get(j,[0, 0])
                dist_r3[j] = [sum + qual_score_r3, counts + 1]
            for j in range(len(read4)):
                qual_score_r4 = bioinfo.convert_phred(read4[j])
                sum, counts = dist_r4.get(j,[0, 0])
                dist_r4[j] = [sum + qual_score_r4, counts + 1]
        index += 1
    print(f"{dist_r3}")
    print(f"{dist_r4}")
    