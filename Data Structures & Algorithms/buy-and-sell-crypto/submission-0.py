class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                buy = -prices[i]
                sell = prices[j]
                current = buy + sell
                if current > best_profit:
                    best_profit = current
                else:
                    continue
        return best_profit