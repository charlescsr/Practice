# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return 0
    
        def levelh(root,val,level):
            if root==None:
                return 0
            
            if root.val==val:
                return level
            
            godown=levelh(root.left,val,level+1)
            
            if godown!=0:
                return godown
            
            godown=levelh(root.right,val,level+1)
            
            return godown
        
        def level(root,val):
            return levelh(root,val,1)
        
        def parent_find(root,val,parent):
            if root==None:
                return 0
        
            if root.val==val:
                return parent
            else:
                p=parent_find(root.left,val,root.val)
                if p!=0:
                    return p
                p=parent_find(root.right,val,root.val)
                
                return p
                             
        return level(root,x)==level(root,y) and parent_find(root,x,-1)!=parent_find(root,y,-1)