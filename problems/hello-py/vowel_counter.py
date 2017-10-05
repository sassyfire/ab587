#!/usr/bin/env python3
"""count your vowels"""


import sys
import os

args = sys.argv[1:]

if len(args) < 1:
    script = os.path.basename(sys.argv[0])
    print('Usage: {} NAME STRING'.format(script))
    sys.exit(1)

word = args[0]

vowels = "aeiou"

count = 0
for char in word:
    if char in vowels:
        count = count + 1

if count == 0:
    print('There are 0 vowels in "{}."'.format(word))
 
elif count == 1:

    print('There is 1 vowel in "{}."'.format(word))

else:

    print('There are {} vowels in "{}."'.format(count, word))
 

#print('word "{}" count "{}"'.format(word, count))

#print('There are 0 vowels in "{}."'.format(word))

#if count == 1:

 #print('There is 1 vowel in "{}."'.format(word))
#elif count == 0:
#    print('zero')
#else:

 #print('There are {} vowels in "{}."'.format(count, word))

#print('word {} count {}'.format(word, count))

#print('There is 1 vowel in "{}."'.format(args))


#if vowels in char > 1:
#        count = count + 1

#print('There are {} vowels '.format(count) + 'in "{}."'.format(args))
