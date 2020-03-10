def rotLeft(a, d):
    for i in range(d):
        tmp=a[0]
        del a[0]
        a.append(tmp)   
    return a