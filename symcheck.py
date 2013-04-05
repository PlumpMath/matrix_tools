#!/usr/bin/env python
''' Usage: symcheck [FILE]

    Options:
      FILE    input file containing the matrix to check for symmetricity
               (if not given, default is stdin).
'''
from docopt import docopt
import scipy
import sys
from matrix_io import read_square_matrix, print_matrix

def main(f):
    mat = read_square_matrix(f)
    sym = mat - mat.transpose()

    #print sym
    print_matrix(sym)

if __name__ == '__main__':
    args = docopt(__doc__)
    #print args
    if args['FILE'] == None:
        main(sys.stdin)
    else:
        main(open(args['FILE'], 'r'))
