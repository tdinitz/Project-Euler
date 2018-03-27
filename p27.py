# p27.py
# created 2017.05.13 by tom and stacy <3

from numpy import *
from primes import get_primes

# have b go through list of primes for 1 to 1000
# have a go from -b to 1000
# factor f(n)=n^2+an+b
# get minimum positive root (if it exists)
# check if that number is greater than current maximum
# if it is, start going through f(n) for n=0,1,2,... and find first non-prime

max_prime=1000
primes,max_prime = get_primes(1000)
maxn=40
maxp=41

for b in primes[primes < 1000]:
    for a in range(-b,1001):
        if a**2-4*b>=0 and (-a-sqrt(a**2-4*b))/2>0 and (-a-sqrt(a**2-4*b))/2<maxn:
            continue
        #quadratic=arange(maxn)**2+a*arange(maxn)+b
        #for inum,num in enumerate(quadratic):
        n=-1
        while True:
            n+=1
            num=n**2+a*n+b
            if num<=0: break
            if num > max_prime:  primes,max_prime=get_primes(num)
            if num not in primes:
                if n > maxn:
                    print 'a',a,'b',b,'n',n
                    maxn = n
                    maxp = a*b
                break
        
print 'maxn',maxn,'maxp',maxp
