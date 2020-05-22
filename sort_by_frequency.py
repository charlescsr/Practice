class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        res=""
        for i,j in c.most_common():
            res+=i*j
        return res