def main():
    for _ in range(int(input())):
        N=int(input())
        g_rev=list(map(int,input().split()))
        opps=list(map(int,input().split()))
        wins=[0,0]
        for i in range(N):
            if g_rev[i]>opps[i]:
                wins[0]+=1
        c=0
        g_rev.sort(reverse=True)
        opps.sort(reverse=True)
        p=0
        for i in range(N):
            for j in range(p,N):
                if g_rev[i]>opps[j]:
                    p=j+1
                    c+=1
                    break
        wins[1]=c
        print(max(wins))

main()