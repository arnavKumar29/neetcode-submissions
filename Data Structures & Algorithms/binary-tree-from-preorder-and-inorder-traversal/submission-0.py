# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder- ROOT LEFT RIGHT
#INORDER - LEFT ROOT RIGHT

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        rootval=preorder[0]
        root=TreeNode(rootval)
        idx=inorder.index(rootval)
        leftin=inorder[:idx]
        rightin=inorder[idx+1:]
        leftpre=preorder[1:1+len(leftin)]
        rightpre=preorder[1+len(leftin):]
        root.left=self.buildTree(leftpre,leftin)
        root.right=self.buildTree(rightpre,rightin)
        return root
                
                

        