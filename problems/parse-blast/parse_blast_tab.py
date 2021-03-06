#!/usr/bin/env python3

import argparse
import os
import sys

#------------------
def get_args():
    parser = argparse.ArgumentParser(description='BLAST tab output')
    parser.add_argument('-p', '--pct_id', help='Percent identity',
                        metavar='float', type =float, default=0.00)
    parser.add_argument('-e', '--evalue', help='',
                        metavar='float', type=float, default=None)
    parser.add_argument('file', metavar='file', help ='BLAST tab output')
    return parser.parse_args()

#-----------------
def main():
    args = get_args()
    pct_id = args.pct_id
    evalue = args.evalue
    blast_file = args.file
    flds = 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'.split()
    
    if not os.path.isfile(blast_file):
        print('"{}" is not a file'.format(blast_file))
        sys.exit(1)
    
    for line in open(blast_file):
        vals = line.rstrip().split('\t')
        rec = dict(zip(flds, vals))
        rec_pident = float(rec['pident'])
        rec_evalue = float(rec['evalue'])
        if rec_pident < pct_id:
            continue
        if evalue is not None and rec_evalue >= evalue:
            continue
        print('\t'.join([rec['qseqid'], rec['sseqid'], rec['pident'], rec['evalue']
]))

 
#-----------------
if __name__ == '__main__':
    main()
