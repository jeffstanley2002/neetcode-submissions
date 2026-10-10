class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(f"{len(i)}#{i}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res=[]

        i=0
        while i <len(s):
            
            delim=s.index('#',i)
            #print(s[i:delim])
            length = int(s[i:delim])
            #print(length)
            #print(s[i:i+delim+length+1])
            val = s[delim+1:delim+1+length]
            #print(val)
            res.append(val)
            i+=delim-i+length+1
        return res



