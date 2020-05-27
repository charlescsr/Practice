import numpy as np
def main():
    N=int(input())
    req=np.array(list(map(int,input().split())))
    qua=np.array(list(map(int,input().split())))
    r=0
    while 0 not in qua:
        qua=np.subtract(qua,req)
        r+=1
    print(r)


main()