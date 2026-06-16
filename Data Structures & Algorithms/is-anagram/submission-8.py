class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        mp2={}
        for letters in s:
            if letters not in mp:
                mp[letters]=1
            else:
                mp[letters]+=1
        for letters in t:
            if letters not in mp2:
                mp2[letters]=1
            else:
                mp2[letters]+=1
        return True if mp==mp2 else False