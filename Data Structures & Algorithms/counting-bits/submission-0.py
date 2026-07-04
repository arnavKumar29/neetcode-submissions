class Solution:
    def countBits(self, n: int) -> List[int]:
        count=0
        binary=[]
        for i in range(n+1):
            binary.append(bin(i).count('1'))

        return binary

            
        