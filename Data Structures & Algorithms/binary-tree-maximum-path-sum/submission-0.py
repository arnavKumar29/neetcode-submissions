# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        summ=-float('inf')
        def dfs(root):
            nonlocal summ
            if not root:
                return 0
            left=self.maxi(root.left)
            right=self.maxi(root.right)
            summ=max(summ,root.val+left+right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return summ
    def maxi(self, root):
        if not root:
            return 0
        left=self.maxi(root.left)
        right =self.maxi(root.right)
        follow=root.val+max(left,right)
        return max(0,follow)



        