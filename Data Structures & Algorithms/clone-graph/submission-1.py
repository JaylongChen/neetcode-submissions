"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # mapping old nodes to new nodes using a hashmap
        oldToNew = {}

        def dfs(node):
            # base case - return the new clone node
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            # map to the new node
            oldToNew[node] = copy
            for n in node.neighbors:
                # cloning the neighbors recursively, and adding to the neighbors
                copy.neighbors.append(dfs(n))

            return copy

        if node:
            return dfs(node)
        else:
            return None