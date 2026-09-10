class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest=prices[0]
        big=0
        for p in prices:
            lowest = min(lowest,p)
            big = max(big,p-lowest)
        return big