# prob18.py
# created 2015.08.29

from numpy import array,concatenate
from sys import *


if len(argv) != 2:
    print '{0} [inputfn]'.format(argv[0])

inputfn = argv[1]

f = open(inputfn,'r')
vals = array([])

for line in f:
    newvals = array([int(val) for val in line.split(' ')])

    if len(newvals)==1:
        vals = newvals
        continue

    vals = array([(a if a>b else b) for a,b in zip(concatenate((vals+newvals[:-1],[0])),concatenate(([0],vals+newvals[1:])))])
    print max(vals),' | ',' '.join([str(val) for val in vals])


f.close()
