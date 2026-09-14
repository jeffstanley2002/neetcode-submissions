from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        d={'[':']','(':')','{':'}'}

        if len(s)%2!=0:
            return False
        
        st=[]
        for i in s:
            if i in d:
                st.append(i)
            else:
                if st!=[] and d[st.pop()]!=i:
                    return False
                
        if all(i not in d for i in s) or st!=[]:
            return False
        return True
        
        

        

        

        