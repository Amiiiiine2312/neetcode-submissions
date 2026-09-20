# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reverse_copy = self.reverse(head)
        if n == 1:
            reverse_copy = reverse_copy.next
        else:
            curr = reverse_copy
            for _ in range (n-2):
                curr = curr.next
            curr.next = curr.next.next

        return self.reverse(reverse_copy)
