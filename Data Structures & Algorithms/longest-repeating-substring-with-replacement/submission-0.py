class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        l=0
        maxc=0

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r],0)+1
            maxc = max(maxc,dic[s[r]])

            if r-l+1-maxc>k:
                dic[s[l]]-=1
                l+=1
        return len(s)-l
          


            

                

        