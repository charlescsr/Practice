#user pantileja
class Solution:
    def checkValidString(self, s: str) -> bool:
        lb=rb=0
        
        n=len(s)
        
        for i in range(n):
            if(s[i] in "(*"):
                lb+=1
            else:
                lb-=1
            if(s[n-i-1] in "*)"):
                rb+=1
            else:
                rb-=1
                
            if(lb<0 or rb<0):
                return False
        
        return True
            