from collections import Counter
x=int(input())
shoes=list(map(int,input().split()))
y=Counter(shoes)
s=0
t=[]
for i in range(int(input())):
    t1,t2=input().split()
    if((int(t1) in y.keys()) and (y[int(t1)]>0)):
        s+=int(t2)
        y[int(t1)]-=1

print(s)