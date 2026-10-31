# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n=0
        cur=head
        while cur:
            cur=cur.next
            n+=1
        
        mid=(n+1)//2
        middle=head
        prev=None
        
        i=0
        while i<mid:
            prev=middle
            middle=middle.next
            i+=1
        prev.next=None
        print(prev.val)

        
        end=None
        while middle:
            nex = middle.next
            middle.next=end
            
            end=middle
            middle=nex
        
        start=head
        while end:
            nex=start.next
            prev=end.next
            start.next=end
            end.next=nex
            start=nex
            end=prev
        
        






        

       
        





        