# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        h=head#0
        prev=None
        while h.next:#1
            nex = h.next #1
            h.next=prev
            prev=h
            h = nex
        h.next=prev  
        return h

            



        