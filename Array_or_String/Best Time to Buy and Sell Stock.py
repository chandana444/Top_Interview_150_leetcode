class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices)<2):
            return 0
        buy=prices[0]
        max_profit=0

        for price in prices[1:]:
            if price<buy: #checking if current price is smaller than prev 
                buy=price 
            
            else:
                profit=price-buy #calculating the profit
                if profit>max_profit: #comparing with max_profit
                    max_profit=profit
        return max_profit

        
