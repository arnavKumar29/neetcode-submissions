class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float('inf')
        maxprice=0
        for i in prices:
            minprice=min(minprice,i)
            maxprice=max(maxprice,i-minprice)
        return maxprice

        