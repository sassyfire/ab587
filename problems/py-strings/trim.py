#!/usr/bin/env python3
"""Sequence Trimmer"""

import sys
import os

args = sys.argv[1:]

if len(args) == 0:
    print('Usage: {} Seq Trim'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

arg = args[0]
input = int(args[1]) if len(args) > 1 else 5

seqs = open(arg) if os.path.isfile(arg) else [arg] 

for seq in seqs:
    print(seq[0:input])

