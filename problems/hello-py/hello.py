#!/usr/bin/env python3
"""say hello to the arguments"""


import sys
import os

args = sys.argv

if len(args) < 1:
    script = os.path.basename(args[0])
    print('Usage: {} NAME [NAME2 ...]'.format(script))
    sys.exit(1)

name = args[1]

if len(args) 
    print('Hello to the {}'.format(len(args[1:])) + ' of you: {}!'.format(', '.join(args[1:])))
