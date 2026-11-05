# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        while queue:
            n = queue.popleft()
            if not n:
                continue
            if n.left and n.right:
                n.left,n.right = n.right,n.left
                queue.append(n.left)
                queue.append(n.right)
                continue
            if n.left:
                n.right=n.left
                queue.append(n.right)
                n.left=None
                continue
            if n.right:
                n.left=n.right
                queue.append(n.left)
                n.right=None
                continue
        return root
        
        