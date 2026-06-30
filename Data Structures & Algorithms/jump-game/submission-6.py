class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump=0
        for i,num in enumerate(nums):
            if i>jump:
                return False
            jump=max(jump,i+num)
        if jump>=len(nums)-1:
            return True
        