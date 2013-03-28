#!/usr/bin/env python

import scipy
import re
import sys

def read_square_matrix(infile):
    ''' Read a matrix from infile which has been printed out in column-
        major form (ie like Fortran). Complain if the number of elements
        is not n**2 for some value of n.
    '''
    try:
        f = scipy.loadtxt((re.sub('[dD]', 'E', line)
            for line in infile))
    except ValueError: # it might be a complex: (real, imag)
        infile.seek(0)
        f = scipy.loadtxt((eval(re.sub('[dD]', 'E', line))[0]
            for line in infile))
    n2 = f.size
    n = scipy.sqrt(n2)
    if n != int(n):
        raise ValueError('Error: nonsquare number of matrix \
                          elements in input: ' + str(n2))
    f = f.reshape(n, n)
    return f

def print_matrix(mat, outfile=sys.stdout, compl=False):
    ''' Print a 2D numpy array in a similar format to the Fortran arrays
        can read in.
    '''
    for row in mat:    # these are COLUMNS of the original fortran array!
        for elem in row:
            if compl:
                outfile.write("({0:22.16E},{1:22.16E})\n".format(elem, 0.0))
            else:
                outfile.write("{0:22.16E}\n".format(elem))
