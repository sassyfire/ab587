#!/usr/bin/env python3
"""say hello to the arguments"""


import sys
import os

args = sys.argv[1:]

if len(args) < 1:
    script = os.path.basename(sys.argv[0])
    print('Usage: {} NAME [NAME2 ...]'.format(script))
    sys.exit(1)

name = args[0]

if len(args) <= 2:
    print('Hello to the {}'.format(len(args)) + ' of you: {}!'.format(' and '.join(args)))
else:
    print('Hello to the {}'.format(len(args)) + ' of you: {}'.format(', '.join(args[:-1])) + ', and {}!'.format(args[-1]))


