class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        sol=[]
        def backtrack(openB,closeB):
            if len(sol)==2*n:
                res.append(''.join(sol))
                return
            if openB<n:
                sol.append('(')
                backtrack(openB+1,closeB)
                sol.pop()
            if openB>closeB:
                sol.append(')')
                backtrack(openB,closeB+1)
                sol.pop()
        backtrack(0,0)
        return res
            
        