import sys

s = input().strip()
try:
    i=int(s)
    print(i)
except Exception:
    print("Bad String")