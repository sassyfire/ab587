#!/usr/bin/env python3
"""hamming"""

#import argparse
import os
import sys
#from Bio import SeqIO

args = sys.argv[1:]

if len(args) < 2:
    print('Usage: {} HAMMING'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

s1 = args[0]
s2 = args[1]

distance = abs(len(s1)-len(s2))

for c1, c2 in zip(s1, s2):
    if c1 != c2:
        distance += 1
print(distance)
#    print('c1 "{}" c2 "{}"'.format(c1, c2))
    




 

  
#for element1, element2 in result:
#     count = 0    
#     print(element1, element2)
    # print('{}'.int(

#---------------------------
#def get_args():
 #   parser = argparse.ArgumentParser(description ='Hamming Distance')
 #   parser.add_argument('-z', '--zap', help='First argument',
 #                       metavar='str', type=str, default='')
 #   parser.add_argument('-d', '--dos', help='Second argument',
 #                       metavar='str', type=str, default='')
 #   return parser.parse_args()

#---------------------------
#def main():
#    """main"""
#    args = get_args()
#    zap = args.zap
#    dos = args.dos
#
#    for args:
#        zap, dos = char.rsplit()
#        result = zip(zap, dos)
#    print(result)
#
#---------------------------
#if __name__ == '__main__':
#    main()
