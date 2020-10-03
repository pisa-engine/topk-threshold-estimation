#!/usr/bin/env python3
from tqdm.notebook import trange, tqdm
import argparse
import itertools


parser = argparse.ArgumentParser(description='Generate pairs and triples from query log.')
parser.add_argument('-q', '--queries', help='a query log file', required=True)
parser.add_argument('-p', '--pairs', help='the pairs output file', required=True)
parser.add_argument('-t', '--triplets', help='the triplets output file', required=True)
args = parser.parse_args()


with open(args.queries) as queries, open(args.pairs, "w+") as pairs_file, open(args.triplets, "w+") as triplets_file:
    line = queries.readline()
    while line:
        text = line.strip()
        terms = set(text.split("\t"))
        for pair in itertools.combinations(terms,2):
            pairs_file.write("\t".join(pair)+"\n")
        for triplet in itertools.combinations(terms,3):
            triplets_file.write("\t".join(triplet)+"\n")
        line = queries.readline()