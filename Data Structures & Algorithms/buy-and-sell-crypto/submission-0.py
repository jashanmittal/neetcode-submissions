class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        n = len(prices)

        for i in range(0, n-1):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                total = max(profit, total)

        return total