# doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # using a hashmap to store the nodes
        self.cache = {} # key, pointers to nodes
        
        # dummy nodes so we dont need to check if null on heads and tails
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    # insert the node at most frequently used (right end)
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.next, node.prev = next, prev
        prev.next = next.prev = node

    def get(self, key: int) -> int:        
        if key in self.cache:
            # need to remove the node from double linked list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        # check exceed capacity
        if len(self.cache) > self.cap:
            lru = self.left.next # left most node (Least recent used)
            self.remove(lru)
            del self.cache[lru.key]
        
