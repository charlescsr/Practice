from itertools import groupby
s=input()
l=[]
keys=[]
for k,v in groupby(s):
    l.append(list(v))
    keys.append(k)
for k,v in zip(keys,l):
    print((len(v),int(k)),end=' ')