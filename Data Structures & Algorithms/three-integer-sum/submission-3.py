class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            goal = -nums[i]

            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[l]+nums[r]==goal and [nums[i],nums[l],nums[r]] not in res:
                    res.append([nums[i],nums[l],nums[r]])
                if nums[l]+nums[r]> goal:
                    r-=1
                else:
                    l+=1
        return res
                



            
        
        