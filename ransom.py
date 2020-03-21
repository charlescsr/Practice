from collections import Counter
def checkMagazine(magazine, note):
    dif=Counter(note)-Counter(magazine)
    if(dif=={}):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    m,n = input().split()

    m = int(m)

    n = int(n)

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
