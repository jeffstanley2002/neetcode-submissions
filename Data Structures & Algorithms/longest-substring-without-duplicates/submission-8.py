class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        res=set()
        temp=-float("inf")
        l=0
        

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l+=1
            res.add(s[r])
            temp=max(temp,r-l+1)
        return temp if temp!=-float("inf") else 0

        