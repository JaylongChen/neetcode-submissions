# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0

        # DFS search for good nodes
        # good node: node that is >= its path nodes
        def countNode(root, max):
            if not root:
                return 
            if root.val >= max:
                self.result += 1
                max = root.val

            countNode(root.left, max)
            countNode(root.right, max)
            

        countNode(root, root.val)
        return self.result