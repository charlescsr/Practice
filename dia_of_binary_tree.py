# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def df(node:TreeNode)->tuple:
            if not node:
                return 0,0
            
            ld=df(node.left)
            rd=df(node.right)
            
            return (
                max(ld[0],rd[0])+1,
                max(ld[1],rd[1],ld[0]+rd[0]+1),
            )
        res=df(root)[1]
        
        if res:
            return res-1
        
        return 0