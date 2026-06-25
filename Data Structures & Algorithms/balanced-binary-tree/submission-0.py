# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def getLength(root):
            if not root:
                return 0

            left = getLength(root.left)
            right = getLength(root.right)

            if abs(right - left) > 1:
                self.result = False
            return 1 + max(left, right)

        getLength(root)
        return self.result
            