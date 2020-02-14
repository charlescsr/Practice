from collections import Counter

k=int(input())
z=map(int,input().split())
zc=Counter(z)

for i in zc:
    if(zc.get(i)==1):
        print(i)