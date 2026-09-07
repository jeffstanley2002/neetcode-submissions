class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        for i,n in enumerate(nums):
            if target-n not in dic:
                dic[target-n]=()
            dic[target-n] = (i,n)
        print(dic.items())
        res=[]
        for i,k in enumerate(nums):
            if k in dic and dic[k][0]!=i:
                res=sorted([dic[k][0],i])
        return res
                
            
        