# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #DFS using stack
        # count=0
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     if node:
        #         count+=1
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return count

        #BFS using queue
        # count=0
        # q=collections.deque()
        # q.append((root))
        # while q:
        #     node=q.popleft()
        #     if node:
        #         count+=1
        #         q.append(node.left)
        #         q.append(node.right)
        # return count

        #Recursive DFS
        if not root:
            return 0
        return (self.countNodes(root.left)+self.countNodes(root.right)+1)

