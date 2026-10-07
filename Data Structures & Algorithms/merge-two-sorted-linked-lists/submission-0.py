# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res=ListNode()
        h=res
        l1,l2=list1,list2
        while l1 and l2:
            if l1.val < l2.val:
                n = l1.next
                l1.next=None
                res.next=l1
                res = res.next
                l1=n
            else:
                n = l2.next
                l2.next=None
                res.next=l2
                res=res.next
                l2=n
        if l1:
            res.next=l1
        else:
            res.next=l2
        return h.next
        


            
        