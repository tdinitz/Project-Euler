from numpy import *


n=10000+1
divisors=zeros(n,dtype=int)

for i in range(1,n):
    divisors[2*i::i]+=i;

print sum([i for i in range(1,n) if divisors[i]<n and divisors[i]!=i and divisors[divisors[i]]==i])

totalsum=0

for i in range(1,n):
    sum=divisors[i]
    if sum<n and sum!=i and divisors[sum]==i:
        totalsum+=i

print totalsum
