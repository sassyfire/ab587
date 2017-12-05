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
    common_keys = set.intersection(*tuple(set(suffixes.keys()) for suffixes in [suffixes, prefixes]))
    for common_keys in suffixes, prefixes:
         if len(record.id) > 1:
             print('{}'.format(record.id))
         else:
             print('no')
#         print('suf {} pre {} common {}'.format(suffixes, prefixes, common_keys))
#    for record.seq in suffixes:
#        if  in prefixes:
#            continue
#        if :
#            print('{}'.format(record.id))
#print('SUFFIX {} PREFIX {}'.format(list(suffixes), list(prefixes)))       
#print('{}:{}'.format(record.id, (list(set(list(suffixes)).intersection(list(prefixes))))))
#    for record.seq in suffixes:
#        if record.seq in prefixes:
#            print('{} {}'.format(record.seq, record.id))
#        else:
#            print('no')

#print record ids of the suffix sequence and prefix sequence

#    for record.seq in sorted(suffixes.items()):
#        if record.seq in sorted(prefixes.items()):
#            print('{}'.format(record.id))

#    print('suf {} pre {}'.format(sorted(suffixes.items()), sorted(prefixes.items())))

#print('{} {}'.format(suffixes, prefixes))
#pairs = list(zip(suffixes.items(), prefixes.items()))
#pairs = list(zip(suffixes, prefixes))
#print(' {} {} '.format(suffixes, prefixes)) 
    


#open a file and make sure it is a file read an open file as long as two sequences 
#are not the same, match the suffix of one sequence to the prefix of another
#print the sequence ids in that respective order
