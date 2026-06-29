class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin=currmax=ans=nums[0]
        for i in range(1,len(nums)):
            temp=currmax
            currmax=max(nums[i],currmax*nums[i],currmin*nums[i])
            currmin=min(nums[i],temp*nums[i],currmin*nums[i])
            ans=max(ans,currmax,currmin)
        return ans