n= int(input())
t=n
for i in range(1,n+1):
    for j in range(i,n+1):
        if j<=i:
            print(j,end=" ")
            t1=j
        else:
            print(t1+t,end=" ")
            t1=t1+t
            t-=1
    t=n
    print()