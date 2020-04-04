import os
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    l=dict.fromkeys((chr(x) for x in range(ord('a'),ord('z')+1)),None)    
    x=dict(zip(l,h))
    m=-sys.maxsize
    for i in range(len(word)):
        if(x.get(word[i])>m):
            m=x.get(word[i])
    return m*len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()