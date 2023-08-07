# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #DFS using stack
        # stack,res=[root],0
        # while stack:
        #     node=stack.pop()
        #     if node:
        #         if not node.right and not node.left:
        #             res+=node.val
        #         if node.right:
        #             node.right.val+=node.val*10
        #             stack.append(node.right)
        #         if node.left:
        #             node.left.val+=node.val*10
        #             stack.append(node.left)
        # return res

        #BFS using Queue
        # q,res=collections.deque([root]),0
        # while q:
        #     node=q.popleft()
        #     if node:
        #         if not node.right and not node.left:
        #             res+=node.val
        #         if node.right:
        #             node.right.val+=node.val*10
        #             q.append(node.right)
        #         if node.left:
        #             node.left.val+=node.val*10
        #             q.append(node.left)
        # return res

        #DFS using Stack(str and int conversion)
        res=0
        stack=[[root,str(root.val)]]
        while stack:
            node,s=stack.pop()
            if node:
                if not node.right and not node.left:
                    res+=int(s)
                if node.left:
                    stack.append([node.left,s+str(node.left.val)])
                if node.right:
                    stack.append([node.right,s+str(node.right.val)])
        return res
        


