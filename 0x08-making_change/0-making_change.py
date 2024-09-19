#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):
    # Base case: If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Create an array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed for total 0

    # Iterate over each amount from 1 to total
    for i in range(1, total + 1):
        # Try each coin and update dp[i]
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be made with given coins
    return dp[total] if dp[total] != float('inf') else -1

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7 (e.g., 25 + 10 + 2)
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1 (total cannot be reached)

