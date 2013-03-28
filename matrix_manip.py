#!/usr/bin/env python

import scipy
import sys
from matrix_io import read_square_matrix, print_matrix

def trim_matrix_asymmetric(m, colsoffleft, rowsofftop,
                           colsoffright, rowsoffbot):
    n = m.shape[0]
    m = m[colsoffleft:(n-colsoffright),rowsofftop:(n-rowsoffbot)]
    return m

def trim_matrix(m, offleft, offright):
    return trim_matrix_asymmetric(m, offleft, offleft, offright, offright)

if __name__ == '__main__':
    m = read_square_matrix(sys.stdin)
    colsoffleft = int(sys.argv[1]) #THESE ARE  FORTRAN ROWS AND COLS!!!
    rowsofftop = int(sys.argv[2])
    colsoffright = int(sys.argv[3])
    rowsoffbot = int(sys.argv[4])
    print_matrix(trim_matrix_asymmetric(m, colsoffleft, rowsofftop,
                                        colsoffright, rowsoffbot))
