class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0]*len(temperatures)
        stack=[]
        for i,n in enumerate(temperatures):
            while stack and n> temperatures[stack[-1]]:
                cur = stack.pop()
                dp[cur] = i-cur
            stack.append(i)
        return dp
            

        



        