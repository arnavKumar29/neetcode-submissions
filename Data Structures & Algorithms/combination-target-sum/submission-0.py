class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol=[]
        res=[]
        n=len(nums)
        def backtrack(i,total):
            if total==target:
                res.append(sol[:])
                return
            if total>target or i==n:
                return
            backtrack(i+1,total)
            sol.append(nums[i])
            backtrack(i,total+nums[i])
            sol.pop()
        backtrack(0,0)
        return res
