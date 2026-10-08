class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(f"{len(i)}#{i}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i=0
        final=[]
        while i< len(s):
            cur=s[i]
            delim = s.index('#',i)
            #print(s,i,delim)
            length = int(s[i:delim])
            res = s[delim+1:delim+1+length]
            #print(length)
            final.append(res)
            i+=(delim-i)+length+1
            #print(s[i],i)
        return final

