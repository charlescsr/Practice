from collections import namedtuple
n,cat=int(input()),input().split()
grade=namedtuple('Grade',cat)
marks=[int(grade._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks)/n)