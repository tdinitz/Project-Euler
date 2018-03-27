# prob20.py
# created 2015.09.05

from numpy import array,concatenate
from sys import *


if len(argv) != 2:
    print 'usage: {0} [n]'.format(argv[0])
    exit()

n = int(argv[1])

vals = array([1])

for i in range(1,n+1):

    vals *= i
    vals = []
    print max(vals),' | ',' '.join([str(val) for val in vals])


f.close()
