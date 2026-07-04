class Solution:
    def reverse(self, x: int) -> int:
        text = str(x)
        
        if x < 0:
            reversed_text = '-' + text[1:][::-1]
        else:
            reversed_text = text[::-1]
            
        res = int(reversed_text)
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
