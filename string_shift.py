class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def lshift(s,amount):
            l=[]
            for i in s:
                l.append(i)
            for i in range(amount):
                l.append(l.pop(0))
            return ''.join(l)
        def rshift(s,amount):
            l=[]
            for i in s:
                l.append(i)
            for i in range(amount):
                l.insert(0,l.pop(-1))
            return ''.join(l)
        for i in shift:
            if(i[0]==0):
                s=lshift(s,i[1])
            else:
                s=rshift(s,i[1])
        return s