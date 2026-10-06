class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0

        def binary_search(lis):
            l,r=0,len(lis)-1

            while l<=r:
                mid=(l+r)//2
                #print(l,r,mid)
                if nums[mid]==target:
                    return mid
                
                if nums[l] <= nums[mid]:
                    if nums[l] <= target <=nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                else:
                    if nums[mid]<=target<=nums[r]:
                        l=mid+1
                    else:
                        r=mid-1

                
            return -1
        return binary_search(nums)
                    

        