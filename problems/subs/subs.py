#!/usr/bin/env python3
"""subs"""

import os
import sys

args = sys.argv[1:]

if len(args) != 2:
    print('Usage: {} STRING SUBS-STRING'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

seq = args[0]
sub = args[1]

if len(sub) > len(seq):
    print('sub > seq'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if len(seq) > 1000:
    print('1 KB'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

indices = []
index = -1
while True:
    index = seq.find(sub, index + 1)
    if index == -1:
        break
    indices.append(index)
indices_2 = [index + 1 for index in indices]

if len(indices_2) > 0:
    print(' '.join(map(str, indices_2)))    
else:
    print('Not found')
   

#pos = seq.index(sub) + 1 #problem- not iterable
#if sub in seq:
#    print('{}'.format(pos))
#else:
#    print('no match')

#you have a sequence and subsequence
#you need to print the position at which each subsequence occurs in the sequence
#position of character in the string
#if the subsequence does not occur, print 'no match'
