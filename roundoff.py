n=int(input())
grades=[]

for i in range(n):
    grades.append(int(input()))

for i in grades:
    if(i<38 or i%5<3):
        print(i)
    else:
        print(i+(5-(i%5)))