from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
            
        t_count = Counter(t)
        window_count = {}
        
        required = len(t_count)
        formed = 0
        
        ans = (float("inf"), 0, 0)
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
                
            while l <= r and formed == required:
                char_l = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                window_count[char_l] -= 1
                if char_l in t_count and window_count[char_l] < t_count[char_l]:
                    formed -= 1
                    
                l += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
