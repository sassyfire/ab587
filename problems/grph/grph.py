#!/usr/bin/env python3

import os
import sys
from Bio import SeqIO
from collections import defaultdict

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]

if not os.path.isfile(file):
    print('"{}" is not a file'.format(file))
    sys.exit(1)

#def sequence_graph(file):
seq_records = SeqIO.parse(file, "fasta")
seq_suf = []
seq_pre = []
suffixes = defaultdict(list)
prefixes = defaultdict(list)
for record in seq_records:
    seq_suf = str(record.seq[-3:])
    seq_pre = str(record.seq[0:3])
    suffixes[seq_suf].append(record.id)
    prefixes[seq_pre].append(record.id)

for suffix in suffixes.keys():
    if suffix in prefixes:
         for rec_id1 in suffixes[suffix]:
              for rec_id2 in prefixes[suffix]:
                  if rec_id1 != rec_id2:
                      print('{} {}'.format(rec_id1, rec_id2))

#open a file and make sure it is a file read an open file as long as two sequences 
#are not the same, match the suffix of one sequence to the prefix of another
#print the sequence ids in that respective order
