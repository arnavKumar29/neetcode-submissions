class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol=[]
        res=[]
        n=len(s)
        def palindrome(l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def backtrack(i):
            if i==len(s):
                res.append(sol[:])
                return
            for j in range(i,len(s)):
                if palindrome(i,j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()
        backtrack(0)
        return res


