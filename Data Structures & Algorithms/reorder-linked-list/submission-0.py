# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        cur=head
        l=0
        while cur:
            l+=1
            cur=cur.next
        midL = (l)//2
        mid=head
        start=mid
        count=0

        while count < midL:
            count+=1
            mid=mid.next
        
        cur=mid
        #mid.next=None
        #print(mid.val,mid.next.val)
        nMid = None

        while cur:
            nex = cur.next
            cur.next = nMid
            nMid = cur
            cur=nex
        
        #start and nMid

        dummy=ListNode()
        cur=head
        while nMid:
            if cur is nMid or cur.next is nMid:
                break
            nex = cur.next
            midN = nMid.next
            cur.next=nMid
            nMid.next=nex
           
            cur=nex
            nMid=midN
        
        





        