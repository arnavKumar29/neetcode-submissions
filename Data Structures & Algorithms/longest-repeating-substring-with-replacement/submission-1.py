class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l =0 
        maxFreq= 0
        maxLen = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) +1
            maxFreq = max(maxFreq, charMap[s[r]])

            while l<r and (r-l+1) - maxFreq > k:
                charMap[s[l]] -=1
                l+=1

            maxLen = max(maxLen, (r-l+1))
        return maxLen