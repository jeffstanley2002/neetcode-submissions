class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        blah2=list(tuple(nums))
        blah=list(tuple(nums))

        cur=blah2[0]
        blah2[0]=1
        res=[1 for i in range(len(blah2))]

        for i in range(1,len(blah2)):
            val=blah2[i]
            blah2[i]=cur
            cur = cur*val
        #print(blah2) 

        cur2=blah[-1]
        blah[-1] = 1
        for i in range(len(blah)-2,-1,-1):
            val=blah[i]
            blah[i]=cur2
            cur2 = cur2*val
        #print(blah) 

        for i,n in enumerate(blah):
            blah2[i]*=n
        return blah2


            
            
            
        
            
        

        