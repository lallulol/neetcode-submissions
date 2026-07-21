class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        best_profit = 0
        while sell < len(prices):
            if prices[buy]>prices[sell]:
                buy = sell
            else:
                profit = prices[sell]-prices[buy]
                best_profit = max(profit, best_profit)
            sell+=1
        return best_profit