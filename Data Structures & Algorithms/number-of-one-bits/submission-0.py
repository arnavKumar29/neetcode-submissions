class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        text=bin(n)
        m=len(text)
        for i in range(m):
            if text[i]=='1':
                count+=1
        return count
                
