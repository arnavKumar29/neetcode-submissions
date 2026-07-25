class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M=len(matrix)
        N=len(matrix[0])
        dp=[[0]*N for i in range (M)]
        if not matrix or not matrix[0]:
            return 0
        def dfs(i,j):
            if not dp[i][j]:
                val=matrix[i][j]
                dp[i][j]=1+max(
                    dfs(i-1,j) if i and val>matrix[i-1][j] else 0,
                    dfs(i+1,j) if i<M-1 and val>matrix[i+1][j] else 0,
                    dfs(i,j-1) if j and val>matrix[i][j-1] else 0,
                    dfs(i,j+1) if j<N-1 and val>matrix[i][j+1] else 0

                )
            return dp[i][j]
        max1=0
        for x in range(M):
            for y in range(N):
                curr=(dfs(x,y))
                max1=max(curr,max1)
        return max1