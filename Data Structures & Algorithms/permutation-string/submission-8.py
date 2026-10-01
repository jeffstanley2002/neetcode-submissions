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
                if cur[s2[l]] == 0:
                    del cur[s2[l]]
                l+=1
            cur[s2[r]] = cur.get(s2[r],0)+1
            print(test,cur)
            if cur==test:
                return True
        return False
            
        