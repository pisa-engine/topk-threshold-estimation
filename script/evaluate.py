#!/usr/bin/env python3

import argparse
import os
import numpy as np

def compute_percentage_overestimate(original, estimated):
    total = 0
    overestimates = 0
    with open(original, 'r') as original_csv, open(estimated, 'r') as estimated_csv:
        for index, (line1, line2) in enumerate(zip(original_csv, estimated_csv)):
            total +=1 
            if float(line1) < float(line2):
                overestimates += 1
    return overestimates/total

def compute_muf(original, estimated):
    under_preds = []
    with open(original, 'r') as original_csv, open(estimated, 'r') as estimated_csv:
        for index, (line1, line2) in enumerate(zip(original_csv, estimated_csv)):
            if float(line2) <= float(line1) and float(line1) != 0:
                under_preds.append(float(line2)/float(line1))
    if len(under_preds):
        return np.mean(under_preds)
    else:
        return 0

parser = argparse.ArgumentParser(description='Evaluation tool.')
parser.add_argument('-e', '--exact', help='the exact thresholds file', required=True)
parser.add_argument('-p', '--predicted', help='the predicted thresholds file', required=True)

args = parser.parse_args()

print("O%: {}".format(round(compute_percentage_overestimate(args.exact, args.predicted),2)))
print("MUF: {}".format(round(compute_muf(args.exact, args.predicted), 2)))
