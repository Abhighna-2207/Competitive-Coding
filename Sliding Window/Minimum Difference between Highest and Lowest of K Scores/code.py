class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        n=len(nums)
        if k==n:
            return max(nums)-min(nums)
        nums.sort()
        c=100000
        for i in range(n-k+1):
            temp=nums[i+k-1]-nums[i]
            if c>temp:
                c=temp
            if c==0:
                return 0
        return c
