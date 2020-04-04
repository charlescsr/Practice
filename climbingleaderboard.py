import os

def climbingLeaderboard(scores, alice):
    i = 0
    j = len(alice)-1
    rank = 1
    ranks = []
    while i<=(len(scores)-1) and j>=0:
        if alice[j]>=scores[i]:
            ranks.append(rank)
            j-=1
        elif alice[j] < scores[i]:
            i+=1
            if i!=0 and i!=len(scores):
                if scores[i]!=scores[i-1]:
                    rank+=1               
    if i==len(scores):
        for x in alice[0:j+1]:
            ranks.append(rank+1)     
    ranks.reverse()
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
