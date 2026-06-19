# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxx):
            if not node:
                return 0
            if node.val>=maxx:
                isGood=1
            else:
                isGood=0
            maxx=max(maxx,node.val)
            return isGood+ dfs(node.left,maxx)+dfs(node.right,maxx)
        return dfs(root,root.val)


            




        