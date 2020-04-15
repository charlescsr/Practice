class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[1 for _ in nums]
        
        l=1
        r=1
        
        for i in range(len(nums)):
            out[i]*=l
            out[-1-i]*=r
            l*=nums[i]
            r*=nums[-1-i]
            
        return out 