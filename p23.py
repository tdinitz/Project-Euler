from numpy import *
#from itertools import combinations_with_replacement

n=28123+1
sums=zeros(n,dtype=int)

for i in range(1,n):  sums[2*i::i]+=i

abundant = where(sums > arange(n))[0]
pairsums = [ abundant[i]+abundant[j] for i in range(len(abundant)) for j in range(i,len(abundant)) if abundant[i]+abundant[j]<n]

nonabundsums = arange(n)
nonabundsums[pairsums] = 0
print nonabundsums
print sum(nonabundsums)


# pairs = list(combinations_with_replacement(abundant, 2))
