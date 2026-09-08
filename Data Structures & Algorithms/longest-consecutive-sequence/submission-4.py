class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        t=set(nums)
        #nums.sort()
        c=0
        for i in nums:
            if i-1 not in t:
                te=i
                cur=0
                while te in t:
                    cur+=1
                    te+=1
                c = max(c,cur)
            
                
        return c

                




        