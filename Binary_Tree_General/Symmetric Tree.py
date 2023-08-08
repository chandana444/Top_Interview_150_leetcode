# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #DFS using Stack
        # stack=[[root.left,root.right]]
        # while stack:
        #     left,right=stack.pop()

        #     if left and right:
        #         if left.val!=right.val:
        #             return False
        #         stack.append([left.left,right.right])
        #         stack.append([left.right,right.left])
        #     elif left or right:
        #         return False
        # return True

        #Recursive DFS
        def isSame(leftroot,rightroot):
            if not leftroot and not rightroot:
                return True
            if not leftroot or not rightroot:
                return False
            if leftroot.val==rightroot.val:
                return isSame(leftroot.left,rightroot.right) and isSame(leftroot.right,rightroot.left)
        
        return isSame(root,root)
