# prob14.py
# created 2015.04.04

from numpy import *
from sys import exit



maxlen = 1
nmax = 1

tested  = [1]
lengths = zeros(int(1e6)+1)
lengths[1] = 1

def find_len(n0):

    if n0 % 2 == 0: n = n0/2
    else:           n = 3*n0 + 1

    if n != 1: return find_len(n)+1
    return 1
    """
    global tested,lengths

    if n0 % 2 == 0: n = n0/2
    else:           n = 3*n0 + 1
    
    if n0 > len(lengths)-1:
        lengths = append(lengths,zeros(n0-len(lengths)+1))

    lengths[n0] = lengths[n]+1 if (n in tested) else find_len(n)+1
    tested += [n0]
    return lengths[n0]
    """

for n0 in range(int(1e6)):

    if n0 % 50000 == 0: print n0,'(',nmax,maxlen,')'

    if n0 < 2: continue
    #if n0 in tested: continue
    
    l = find_len(n0)

    if l > maxlen:
        maxlen = l
        nmax = n0

print nmax, maxlen
