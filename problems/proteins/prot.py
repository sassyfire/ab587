#!/usr/bin/env python3
"""codon table"""

import sys
import os
from collections import Counter
from collections import defaultdict

args = sys.argv[1:]

if len(args) < 1:
   print('Usage: {} SEQ'.format(os.path.basename(sys.argv[0])))
   sys.exit(1)

rna = args[0].upper()

codon_table = dict()

for line in open("codons.rna"):
    codon, protein = line.rstrip().rsplit()
    codon_table[codon] = protein    

k = 3 
proteins = []
for codon in [rna[i:i+k] for i in range(0, len(rna), k)]:
     proteins.append(codon_table[codon])

print(''.join(proteins))
#    print(codon_table[codon], end='')

#print()    

