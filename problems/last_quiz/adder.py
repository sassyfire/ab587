#!/usr/bin/env python3

import sys
import os

args = sys.argv[1:]

if len(args) != 2:
   print('Usage: {} NEED 1 MORE'.format(os.path.basename(sys.argv[0])))
   sys.exit(1)

if type(args[0]) == int and type(args[1]) == str:
    print('Cannot add different types')
    sys.exit(1)	

if type(args[1]) == int and type(args[0]) == str:
    print('Cannot add different types')
    sys.exit(1)



if args[0].isdigit() and args[1].isdigit():
    sum = int(args[0]) + int(args[1])
    print('{}'.format(sum))
elif type(args[0]) == str and type(args[1]) == str:
    print('{} and {}'.format(args[0], args[1]))
else:
    print('cannot add')
#   print('Cannot add {} ({}) and {} ({})'.format(args[0], type[args[0], args[1], type(args[1])))
