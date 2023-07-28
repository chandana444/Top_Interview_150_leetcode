# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS using stack(iterative DFS)
        """stack=[[p,q]]
        while stack:
            node1,node2=stack.pop()
            if not node1 and not node2:
                continue
            elif (not node1 or not node2) or (node1.val!=node2.val):
                return False

            stack.append([node1.left,node2.left])
            stack.append([node1.right,node2.right])
        return True"""

        #RECURSIVE DFS
        if not p and not q:
            return True
        elif(not p or not q) or (p.val!=q.val):
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        #string approach
        """return str(p)==str(q)"""
        


        

