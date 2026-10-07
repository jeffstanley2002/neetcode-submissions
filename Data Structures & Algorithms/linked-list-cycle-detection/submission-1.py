# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        cur=head
        if not cur:
            return False

        while cur.next:
            if cur not in s:
                s.add(cur)
            else:
                return True
            cur = cur.next
        return False
        