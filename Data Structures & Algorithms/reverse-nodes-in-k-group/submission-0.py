# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        # break up the linked list into k groups, reverse the linkedlist in the group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            # reverse the k length sub linkedlist
            prev, curr = kth.next, groupPrev.next            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    # get linkedlist that is kth long
    def getKth(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr
