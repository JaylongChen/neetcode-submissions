"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        buffer = {}  # pointer, value
        curr = head
        # copy nodes to dictionary
        while curr:
            copy = Node(curr.val)
            buffer[curr] = copy
            curr = curr.next

        #connect the copied nodes
        curr = head
        while curr:
            copy = buffer[curr]
            copy.next = buffer.get(curr.next)
            copy.random = buffer.get(curr.random)
            curr = curr.next

        return buffer.get(head)