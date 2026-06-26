class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countofS =Counter(s)
        countofT =Counter(t)
        return countofS==countofT
        