#!/usr/bin/env python
import matplotlib.pyplot as plt
import os
import sys
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Process input files and writes data for per nucleotide quality averages.")
    parser.add_argument('output', type=str, help='The path to the first file.')
    return parser.parse_args()

#parameters
args = get_args()
output = args.output

with open(output, 'r') as f:
    dist_r1 = eval(f.readline().strip())
    dist_r2 = eval(f.readline().strip())
    dist_r3 = eval(f.readline().strip())
    dist_r4 = eval(f.readline().strip())

    #R1
    means =[]
    for key,value in dist_r1.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(150), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for Read 1')
    plt.savefig("r1.png")
    plt.close()

    #R2
    means = []
    for key,value in dist_r2.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(150), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for Read 2')
    plt.savefig("r2.png")
    plt.close()

    #R3
    means = []
    for key,value in dist_r3.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(150), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for Read 3')
    plt.savefig("r3.png")
    plt.close()

    #R4
    means = []
    for key,value in dist_r4.items():
        average = value[0] / value[1]
        means.append(average)
    plt.bar(range(150), means, color="#02D2D2", edgecolor='black')
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.xlabel('Base Position')
    plt.ylabel('Mean')
    plt.title('Distribution of Quality Scores for Read 4')
    plt.savefig("r4.png")
    plt.close()