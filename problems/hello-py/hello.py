#!/usr/bin/env python3
"""say hello to the arguments"""


import sys
import os

def main():
    """main"""
    args = sys.argv

    if len(args) < 1:
        script = os.path.basename(args[0])
        print('Usage: {} NAME [NAME2 ...]'.format(script))
        sys.exit(1)

    print('Hello to the {}'.format(' '.str(args[1:])) + 'of you: {}!'.format(' , , and '.join(args[1:])))

if __name__ == '__main__':
    main()
