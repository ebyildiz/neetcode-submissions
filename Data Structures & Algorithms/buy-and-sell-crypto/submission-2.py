class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            comp = prices[j]-prices[i]
            if comp > max_profit:
                max_profit = comp
            else:
                if prices[j]<prices[i]:
                    i=j
            j+=1
            print(max_profit)
        return max_profit