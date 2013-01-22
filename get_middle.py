#!/usr/bin/env python

import scipy
import matplotlib.pyplot as plt
import sys
import re

def main(infile):
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

    f = abs(f).reshape(n, n).transpose() + 1.0E-5
    plt.imshow(scipy.log(f))
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(sys.stdin)
    else:
        for filename in sys.argv[1:]:
            main(open(filename, 'r'))
