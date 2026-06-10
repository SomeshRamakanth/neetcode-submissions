class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for i in prices:
            if i < low:
                low = i
            profit = max(profit, i - low)
        return profit