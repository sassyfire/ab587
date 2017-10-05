#!/usr/bin/env python3
"""count your vowels"""


import sys
import os

args = sys.argv[1:]

if len(args) < 1:
    script = os.path.basename(sys.argv[0])
    print('Usage: {} NAME STRING'.format(script))
    sys.exit(1)

name = args[0]

vowels = "a", "e", "i", "o", "u"

count = 0
if vowels in args <= 1:
   count = count + 1

print('There is 1 vowel in "{}."'.format(args))

count = 0
if vowels in args !=1:
   count = count + 1

print('There are {} vowels '.format(len(vowels)) + 'in "{}."'.format(args))
