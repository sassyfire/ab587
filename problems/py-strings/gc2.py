#!/usr/bin/env python3
"""Sequence Files"""

import sys
import os

args = sys.argv[1:]

if len(args) == 0:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]

if not os.path.isfile(file):
    print('"{}" is not a file'.format(file))
    sys.exit(1)

for seq in open(file):
    count_gc = 0
    for char in seq:
        if char == 'G' or char == 'g' or char == 'C' or char == 'c' in bases:
            count_gc = count_gc + 1
    print('{}'.format(int((count_gc*100)/(len(seq)-1))))  


#print('"{}" = "{}"'.format(seq, count_gc), end=' ')

#for count_gc in lines:
#    print(count_gc, end=' ')

