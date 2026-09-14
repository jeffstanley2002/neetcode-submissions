class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l=0
        cur=[]
        se1 = list(s1)
        
        for r in range(len(s2)):
            while (r-l+1)>len(s1):
                l+=1
                cur.pop(0)
            cur.append(s2[r])
            if (r-l+1)==len(s1):
                se2=(cur)
                if sorted(se1)==sorted(se2):
                    
                    return True
        return False

            
            
        