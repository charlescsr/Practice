import os

# Complete the timeInWords function below.
def timeInWords(h, m):
    time={
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        21:'twenty one',
        22:'twenty two',
        23:'twenty three',
        24:'twenty four',
        25:'twenty five',
        26:'twenty six',
        27:'twenty seven',
        28:'twenty eight',
        29:'twenty nine',
    }
    if(1<=m and m<=30):
        if(m==30):
            return 'half past '+time.get(h)
        elif(m==15):
            return 'quarter past '+time.get(h)
        elif(m==1):
            return time.get(m)+' minute past '+time.get(h)
        else:
            return time.get(m)+' minutes past '+time.get(h)      
    elif(m==0):
        return time.get(h)+" o' clock"
    else:
        if(m==45):
            return 'quarter to '+time.get(h+1)
        else:
            return time.get(60-m)+' minutes to '+time.get(h+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
