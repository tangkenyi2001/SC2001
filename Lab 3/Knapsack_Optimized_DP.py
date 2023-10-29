# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapsack_unbounded_bottom_up(capacity):
    weights = [5, 6, 8]
    profits = [7, 6, 9]

    n = len(weights)
    # Create a table to store the maximum profit for each capacity
    dp = [0] * (capacity + 1)

    # Iterate over all capacities from 1 to the given capacity
    for i in range(1, capacity + 1):
        # Iterate over all types of objects
        for j in range(n):
            # Check if the weight of the current object is less than or equal to the current capacity
            if weights[j] <= i:
                # Update the maximum profit for the current capacity
                dp[i] = max(dp[i], dp[i - weights[j]] + profits[j])

    # The final result is stored in dp[capacity]
    return dp[capacity]

def get_optimal_items(capacity):
    weights = [5, 6, 8]
    profits = [7, 6, 9]
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(1, capacity + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + profits[j])

    # Backtrack to find the quantities of each item included in the optimal solution
    i = capacity
    quantities = [0] * n
    while i > 0 and dp[i] > 0:
        for j in range(n):
            if weights[j] <= i and dp[i] == dp[i - weights[j]] + profits[j]:
                quantities[j] += 1
                i -= weights[j]

    return quantities

weights = [4, 6, 8]
profits = [7, 6, 9]
total_profit = [0, 0, 0]
capacity = 14
# max_profit = knapsack_unbounded_top_down(capacity)
# print("(Top Down) Maximum profit:", max_profit)

print("Given weights:", weights)
print("Given profits:", profits)
max_profit = knapsack_unbounded_bottom_up(capacity)
print("(Bottom Up) Maximum profit:", max_profit)

optimal_items = get_optimal_items(capacity)
for j in range(len(optimal_items)):
    total_profit[j] = profits[j] * optimal_items[j]
    print(f"Item {j + 1} [Weight: {weights[j]}, Unit Profit: {profits[j]}] {optimal_items[j]} units")

#Print calculation of all profits and the unit costs
print(f"Total profit for Capacity {capacity}: {optimal_items[0]}({profits[0]}) + {optimal_items[1]}({profits[1]}) + {optimal_items[2]}({profits[2]}) = ")
print(f"Total profit for Capacity {capacity}: {total_profit[0]} + {total_profit[1]} + {total_profit[2]} = {sum(total_profit)}")


