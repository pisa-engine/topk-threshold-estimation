#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Drop terms from lexicon.')
parser.add_argument('-d', '--dropped', help='a dropped terms list', required=True)
parser.add_argument('-t', '--terms', help='a lexicon file', required=True)
parser.add_argument('-o', '--output', help='the output file', required=True)

args = parser.parse_args()

dropped_terms = set(line.rstrip() for line in open(args.dropped))
terms = [line.rstrip().rstrip() for line in open(args.terms, 'r')]

print("Dropping {} of {} terms.", len(dropped_terms), len(terms))

with open(args.output, "w") as terms_file:
    for i, term in enumerate(terms):
        if str(i) in dropped_terms:
            continue
        terms_file.write(term+"\n")
