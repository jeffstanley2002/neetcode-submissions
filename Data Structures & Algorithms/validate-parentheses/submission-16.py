class Solution:
    def isValid(self, s: str) -> bool:
        dic={']':'[','}':'{',')':'('}
        if len(s)%2!=0:
            return False
        l=[]

        for i in s:
            #print(l)
            if i not in dic:
                l.append(i)
            else:
                #print(l)
                if l==[]:
                    return False
                cur=l.pop()
                if cur!=dic[i]:
                    return False
            #print(l)
        if l!=[]:
            return False
        return True



        
        