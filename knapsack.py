def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum value will be in the bottom-right cell of the table
    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]  # Item weights
values = [3, 4, 5, 6]   # Item values
capacity = 5            # Knapsack capacity

max_value = knapsack(weights, values, capacity)
print(f"Maximum value in Knapsack: {max_value}")
