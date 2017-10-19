#!/usr/bin/env python3
"""Kmer Counter"""

import sys
import os
from collections import defaultdict

args = sys.argv[1:]
 
if len(args) != 2:
    print('Usage: {} LEN STR'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if not args[0].isdigit():
    print('Kmer size "{}" is not a number'.format(args[0]))
    sys.exit(1)

k = int(args[0])
sequence = args[1]

if k < 1:
    print('Kmer size "{}" must be > 0'.format(k))
    sys.exit(1)

#print('kmer "{}" seq "{}"'.format(k, sequence))

nk = len(sequence) - k + 1

if nk < 1:
   print('There are no {}-mers in "{}"'.format(k, sequence))
   sys.exit(1)

kmers = defaultdict(int)
for i in range(nk):
   kmer = sequence[i:i+k]
   kmers[kmer] += 1

print(sequence)

for kmer, num in sorted(kmers.items()):
    print('{} {}'.format(kmer, num))


