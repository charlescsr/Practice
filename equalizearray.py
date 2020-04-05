from collections import Counter

n=int(input())
arr=list(map(int,input().split()))
c=Counter(arr).values()
ops=len(arr)-max(c)
print(ops)