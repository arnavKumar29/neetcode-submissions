class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maph=Counter(nums)
        for num,freq in maph.items():
            if freq==1:
                return num
