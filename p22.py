file=open('names.txt','r')
names=file.read()
names=sorted(names.split(','))

print sum([(i+1)*sum([ord(c)-ord('A')+1  for c in s[1:-1]]) for i,s in enumerate(names)])



