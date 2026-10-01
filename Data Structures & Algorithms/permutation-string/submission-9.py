class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        test={}
        for i in s1:
            test[i] = test.get(i,0)+1
        

        cur={}
        l=0
        for r in range(len(s2)):
            
            while (r-l+1)>len(s1):
                cur[s2[l]]-=1
                
                l+=1
            cur[s2[r]] = cur.get(s2[r],0)+1
            print(test,cur)
            if all(test[i] == cur.get(i, 0) for i in test):
                return True
        return False
            
        