class Solution:
    def countElements(self, arr: List[int]) -> int:
        c=Counter(arr)
        e=0
        for i in sorted(arr):
            if(c.get(i+1) in c.values() and c.get(i+1)>=1):
                e+=1
        return e 