import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            for j in i:
                s+=str(ord(j))
                s+=','
            s+=' '
        return s

    def decode(self, s: str) -> List[str]:
        
        res=[]
        cur = re.split(r" ",s)[:-1]
        
        for i in cur:
            
            #print(i)
            c2=re.split(r",",i)
            c4=''
            for i in c2:
                if i.isnumeric():
                    c4+=chr(int(i))
            res.append(c4)
        
        return res
