class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(f"{len(i)}#{i}")
        print(''.join(res))
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            delim = s.index("#",i)
            length = int(s[i:delim])
            string = s[delim+1:delim+1+length]
            res.append(string)
            i+=(delim-i)+length+1
        return res

