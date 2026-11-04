# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur=head
        l=0
        while cur:
            cur=cur.next
            l+=1
        rem = l-n
        if rem==0:
            return head.next
        

        
        i=0
        cur=head
        while i < rem-1:
            i+=1
            cur=cur.next
        cur.next = cur.next.next
        return head