# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2=deque(),deque()

        c1=l1
        while c1:
            n1.appendleft(str(c1.val))
            c1 = c1.next
        c2=l2
        while c2:
            n2.appendleft(str(c2.val))
            c2 = c2.next
        tot = str(int(''.join(n1))+int(''.join(n2)))[::-1]
        res=[]
        for i in tot:
            res.append(int(i))
        dummy=ListNode()
        final=dummy
        queue = deque()
        for i in res:
            n=ListNode()
            n.val=i
            queue.append(n)
        
        while queue:
            n=queue.popleft()
            dummy.next=n
            dummy=n
        return final.next
            

        

        