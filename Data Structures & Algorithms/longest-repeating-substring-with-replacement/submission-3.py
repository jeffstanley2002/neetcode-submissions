class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        big=0
        l=0
        dic={}

        for r in range(len(s)):
            
            dic[s[r]] = dic.get(s[r],0)+1
            big = max(big,dic[s[r]])
            #print(dic,big,r,l)
            while r-l+1-big>k:
                dic[s[l]]-=1
                l+=1
        return min(big+k,len(s))
                
        

            

            

        

        

        
                


        