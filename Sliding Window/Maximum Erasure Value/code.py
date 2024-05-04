class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        seen=set()
        res=0
        i=0
        tot=0
        for j in range(len(nums)):
            x=nums[j]
            while i<j and x in seen:
                seen.remove(nums[i])
                tot-=nums[i]
                i+=1
            tot+=x
            seen.add(x)
            res=max(res,tot)
        return res


              


        
