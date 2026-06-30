
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x=len(text1)
        y=len(text2)
        dp = [[0] * (y + 1) for _ in range(x+ 1)]
        for i in range(x-1,-1,-1):
            for j in range(y-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return int(dp[0][0])
