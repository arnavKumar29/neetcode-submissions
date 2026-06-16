class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = nums[0]
        r = nums[0]

        while True:
            l = nums[l]
            r = nums[nums[r]]

            if l == r:
                break

        l = nums[0]

        while l != r:
            l = nums[l]
            r = nums[r]

        return l