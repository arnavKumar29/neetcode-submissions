class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            desired=target-num
            if desired in map:
                return [map[desired],i]
            map[num]=i
        