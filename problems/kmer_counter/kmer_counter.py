#!/usr/bin/env python3
"""Kmer Counter"""

import sys
import os
from collections import Counter

args = sys.argv[1:]

text = ' ' 
if len(args) == 0:
    print('Usage: {} LEN STR'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)
else:
    text = args

count = Counter(text.lower())

num = args[0] 
dna = args[1]

for base in "acgtACGT":
    if num == int(args[0]):
        base = sorted(count.keys())
print('{} {}'.format(num, base))

if num == int(args[0]):
    print('Kmer size "{}" must be > 0"'.format(num))
else:
    print('Kmer size "{}" is not a number"'.format(num))



    counts.append(str(count[base]))
print ('{} {} '.format(num, letter))
