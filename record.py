import os

def breakingRecords(scores):
    br=[0,0]
    mi=scores[0]
    ma=scores[0]
    for i in scores:
        if(i>ma):
            br[0]+=1
            ma=i
        elif(i<mi):
            br[1]+=1
            mi=i
    return br

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
