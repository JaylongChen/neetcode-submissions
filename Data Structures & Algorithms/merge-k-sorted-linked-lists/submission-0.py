# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = []
        

        for l in lists:
            while l:
                heapq.heappush(data, l.val)
                l = l.next

        dummy = ListNode()
        curr = dummy
        
        for i in range(len(data)):
            value = ListNode(heapq.heappop(data))
            curr.next = value
            curr = curr.next
        
        return dummy.next