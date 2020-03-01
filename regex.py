import re
for _ in range(int(input())):  
    try:
        print(bool(re.compile(input())))#re.compile checks if a string is regex or not
    except:
        print('False')