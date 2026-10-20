class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, buy2 = 0,0,0
        n = len(prices)

        for i in range(n-1,-1,-1):
            dp_buy = max(sell-prices[i],buy)
            dp_sell = max(buy2+prices[i],sell)
            buy2 = buy
            buy,sell = dp_buy,dp_sell
        return buy
            

        