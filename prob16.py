# pe.py
# created 2015.08.29

from numpy import *

a = array([2])
print '{0:<4} {1:<4} {2}'.format(0,sum(a),a)

for i in range(2,1001):
    a *=2
    for j in range(len(a)-1,-1,-1):
        if a[j] >= 10:
            a[j] -= 10
            if j==0:
                a = concatenate(([1],a))
            else:
                a[j-1] += 1
    if i % 100 == 0: print '{0:<4} {1:<4} {2}'.format(i,sum(a),a)

print 'sum (at i',i,'is',sum(a)
