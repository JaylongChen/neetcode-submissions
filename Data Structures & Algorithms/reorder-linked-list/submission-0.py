# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the linked list evenly, with 2 pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half linked list
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge two linked list
        l1 = head
        l2 = prev
        while l2:
            temp1, temp2 = l1.next, l2.next
            l2.next = temp1
            l1.next = l2
            l1, l2 = temp1, temp2
            
            


