import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            x1=heapq.heappop(stones)
            x2=heapq.heappop(stones)
            if(x1!=x2):
                heapq.heappush(stones,-abs(x1-x2))
        if len(stones)==0:
            return 0
        
        return -stones[0]   