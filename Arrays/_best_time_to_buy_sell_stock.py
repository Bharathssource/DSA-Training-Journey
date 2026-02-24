# Problem:
# Given an array prices where prices[i] is the price of a stock on day i,
# return the maximum profit from one buy and one sell.
# Approach: Running minimum + running maximum difference (Greedy).
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit
