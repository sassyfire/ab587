#!/usr/bin/env python3
"""GC Content"""

import sys
import os

args = sys.argv[1:]

if len(args) == 0:
    print('Usage: {} GC Content'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

sequence = args[0]
bases = "ATGC"

count_gc = 0

for char in sequence:
    if char == 'G' or char == 'g' or char == 'C' or char == 'c' in bases:
        count_gc = count_gc + 1

print('{}% GC'.format(int(((count_gc)*100)/len(sequence))))
#
