class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
                    return 0

        # Initialize variables
        min_price = prices[0]
        max_profit = 0
        
        # Iterate through prices
        for price in prices[1:]:
            # Update minimum price seen so far
            if price < min_price:
                min_price = price
            else:
                # Calculate potential profit if selling at 'price'
                max_profit = max(max_profit, price - min_price)
        
        return max_profit
            