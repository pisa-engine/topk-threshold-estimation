#!/usr/bin/env python3

import argparse
import os
import numpy as np

def hybridize(first_method, second_method, output):
    with open(first_method, 'r') as first, open(second_method, 'r') as second, open(output, 'w+') as out:
        for (line1, line2) in zip(first, second):
            	out.write(max(line1, line2))
    
parser = argparse.ArgumentParser(description='Hybridize two predictions method.')
parser.add_argument('-f', '--first-method', help='the first method file', required=True)
parser.add_argument('-s', '--second-method', help='the second method file', required=True)
parser.add_argument('-o', '--output', help='the output file', required=True)

args = parser.parse_args()

hybridize(args.first_method, args.second_method, args.output)
