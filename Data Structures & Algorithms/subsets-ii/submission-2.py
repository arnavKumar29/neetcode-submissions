class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        sol=[]
        def backtrack(i):
            if i==n:
                res.append(sol[:])
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        seen=set()


        unique=[]
        for lists in res:
            tupleversion=tuple(lists)
            if tupleversion not in seen:
                seen.add(tupleversion)
                unique.append(lists)
        return unique