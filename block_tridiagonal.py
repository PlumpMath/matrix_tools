#!/usr/bin/env python
''' Usage: btd FILE1 FILE2 <n>

    Options:
      FILE1    input file containing the diagonal block
      FILE2    input file containing the superdiagonal block
      n        the number of blocks along the diagonal of the output
'''
from docopt import docopt
import scipy
import sys
from matrix_io import read_square_matrix, print_matrix

def main(args):
    diag = read_square_matrix(open(args['FILE1'], 'r'))
    offdiag = read_square_matrix(open(args['FILE2'], 'r'))
    n = int(args['<n>'])

    if not (diag.shape == offdiag.shape):
        exit('Matrices are not of equal dimension')

    n_block = diag.shape[0]
    n_mat = n * n_block
    mat = scipy.zeros((n_mat, n_mat))

    for i in range(n):
        mat[i*n_block:(i+1)*n_block, i*n_block:(i+1)*n_block] = diag

    for i in range(n-1):
        mat[(i+1)*n_block:(i+2)*n_block, i*n_block:(i+1)*n_block] = offdiag
        mat[i*n_block:(i+1)*n_block, (i+1)*n_block:(i+2)*n_block] = offdiag.transpose()

    #print mat
    print_matrix(mat)

if __name__ == '__main__':
    args = docopt(__doc__)
    #print args
    main(args)
