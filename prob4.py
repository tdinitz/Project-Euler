# prob4.py
# created 2015.02.21


from sys import *
from numpy import arange,meshgrid


i0,iN = int(argv[1]),int(argv[2])

x = arange(i0,iN+1)
a,b = meshgrid(x,x)
prod = a*b
prod.shape = (prod.size)

for num in prod:
    snum = str(num)
    if (snum[0] == snum[-1]) and (snum[1] == snum[-2]) and (snum[2] == snum[-3]):
        print num

