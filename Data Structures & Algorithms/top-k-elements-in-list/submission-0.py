class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        
        return list(map(lambda x:x[0],sorted(dic.items(),key=lambda x:-x[1])))[:k]
       # return list(map(sorted(dic.items(),key=lambda x:-x[1]),lambda x x:x[0]))[:k]
        