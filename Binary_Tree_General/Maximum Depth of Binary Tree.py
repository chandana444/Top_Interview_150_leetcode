# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #RECURSIVE DFS APPROACH
        """if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))"""

        #BFS APPROACH WHERE WE COUNT LEVELS OF THE TREE BY USING DEQUE
        """if not root:
            return 0
        
        d=deque([root])
        level=0
        while d:
            for i in range(len(d)):
                node=d.popleft()
                if(node.left):
                    d.append(node.left)
                if(node.right):
                    d.append(node.right)
            level+=1
        return level"""

        #ITERATIVE DFS BY USING STACK
        res=0
        stack=[[root,1]]
        while stack:
            node,depth=stack.pop()

            if node:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res


        
                
