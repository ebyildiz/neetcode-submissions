class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = len(prices)-1
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                new_profit = prices[j]-prices[i]
                if new_profit > max_profit:
                    max_profit = new_profit

        return max_profit

