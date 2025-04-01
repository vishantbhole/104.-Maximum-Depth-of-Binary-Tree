# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        stack = [[root,1]]
        res = 0
        while stack:
            root, depth = stack.pop()
            if root:
                res = max(res,depth)
                stack.append([root.left,depth + 1])
                stack.append([root.right,depth + 1])
        return res
        
