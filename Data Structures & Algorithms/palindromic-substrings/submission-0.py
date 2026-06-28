class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            r=i
            l=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                count+=1
                l-=1
                r+=1
            r=i+1
            l=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                count+=1
                l-=1
                r+=1
        return count
            
            