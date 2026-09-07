class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = {}
        l2={}
        for i in s:
            if i not in l1:
                l1[i]=0
            l1[i]+=1
        for i in t:
            if i not in l2:
                l2[i]=0
            l2[i]+=1
        l1 = sorted(list(l1.items()))
        l2 = sorted(list(l2.items()))
        return l1==l2
       

        