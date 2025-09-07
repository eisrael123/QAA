#!/usr/bin/env python

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Checks the number of reads that are properly mapped to the reference genome and number of reads that aren't.")
    parser.add_argument("-f", help="Specify the filepath of the SAM file", required=True, type=str)
    return parser.parse_args()

args = get_args()

mapped = 0
unmapped = 0
with open(args.f,"r") as in_file: #open input SAM file
    for line in in_file: #iterate each line
        if line[0] != "@": #if its not a header
            flag = int(line.split()[1]) #extract bit-wise number (2nd column)
            if (flag&4) != 4 and (flag&256) != 256:#check if its mapped AND not a secondary alignment
                mapped += 1
            if (flag&4) == 4 and (flag&256) != 256:#check if its unmapped AND not a secondary alignment
                unmapped += 1
print(f"Counts for {args.f}")
print(f"Mapped reads = {mapped}")
print(f"Unmapped reads = {unmapped}")