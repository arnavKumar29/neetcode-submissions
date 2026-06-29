class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        half=sum(nums)//2
        
        dp=[False]*(half+1)
        dp[0]=True
        for num in nums:
            for i in range(half,num-1,-1):
                dp[i]=max(dp[i],dp[i-num])
        return dp[half]
