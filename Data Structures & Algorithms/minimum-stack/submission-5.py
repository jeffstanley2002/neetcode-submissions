from collections import deque
class MinStack:

    def __init__(self):
        self.stack= collections.deque()
        self.sm = collections.deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        v = min(val,self.sm[-1]) if self.sm else val
        self.sm.append(v)

        

    def pop(self) -> None:
        self.sm.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.sm[-1]

        
