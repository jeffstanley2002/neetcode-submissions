from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+':lambda x,y:x+y,'-':lambda x,y:y-x,'*':lambda x,y:x*y,'/':lambda x,y:y/x}
        queue = []

        for i in tokens:
            if i not in ops:
                queue.append(i)
            else:
                n1,n2=int(queue.pop()),int(queue.pop())
                #print(n1,n2,i)
                val=ops[i](n1,n2)
                queue.append(val)
        return int(queue[-1])




        