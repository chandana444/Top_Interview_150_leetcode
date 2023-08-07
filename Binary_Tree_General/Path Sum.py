# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Recursive DFS
        # if not root:
        #     return False
        # if not root.right and not root.left and root.val==targetSum:
        #     return True
        # return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

        #DFS using Stack
        # stack=[[root,targetSum]]
        # while stack:
        #     node,s=stack.pop()
        #     if node:
        #         if not node.right and not node.left and node.val==s:
        #             return True
        #         if node.left:
        #             stack.append([node.left,s-node.val])
        #         if node.right:
        #             stack.append([node.right,s-node.val])
        # return False

        #BFS using Queue
        q=collections.deque()
        q.append((root,targetSum))
        while q:
            node,s=q.popleft()
            if node:
                if not node.right and not node.left and node.val==s:
                    return True
                if node.left:
                    q.append((node.left,s-node.val))
                if node.right:
                    q.append((node.right,s-node.val))
        return False
    
