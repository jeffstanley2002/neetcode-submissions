# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        dummy=None
        cur=head
        if not cur:
            return cur
        while cur.next:
            temp=cur.next
            cur.next=dummy
            dummy=cur
            cur=temp
        cur.next=dummy
        return cur
        