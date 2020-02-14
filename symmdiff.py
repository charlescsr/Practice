m=int(input())
s=list(map(int,input().split()))
n=int(input())
s1=list(map(int,input().split()))
s.sort()
s1.sort()
r1=set(s)
r2=set(s1)
res=sorted(r1.symmetric_difference(r2))

for i in res:
    print(i)