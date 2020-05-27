n=int(input())
t=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print(i,end=" ")
        elif j==1:
            print(1,end=" ")
            t=1
        else:
            t+=1
            print(t,end=" ")
    print()