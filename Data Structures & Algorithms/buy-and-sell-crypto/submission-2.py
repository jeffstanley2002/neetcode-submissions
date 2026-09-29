class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=-float("inf")
        minp=float("inf")
        res=-float("inf")
        for p in prices:
            if p < minp:
                minp = min(p,minp)
            else:
                res = max(res,p-minp)
            
        return res if res != -float("inf") else 0


        