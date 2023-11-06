import timeit
import sys


def unboundedKnapsack(c, w, p, idx, dp, selected_items):
    if idx == 0:
        if c >= w[0]:
            selected_items[idx] += c // w[0]
        return (c // w[0]) * p[0]
    
    if dp[idx][c] != -1:
        return dp[idx][c]

    notTake = 0 + unboundedKnapsack(c, w, p, idx - 1, dp, selected_items)

    take = float('-inf')
    if w[idx] <= c:
        take = p[idx] + unboundedKnapsack(c - w[idx], w, p, idx, dp, selected_items)
        
    if take > notTake:
        selected_items[idx] += 1  # Add the current item to the selection

    dp[idx][c] = max(take, notTake)
    return dp[idx][c]

def traceSelectedItems(capacity, weights, profits, dp):
    n = len(profits)
    selected_items = [0] * n

    for i in range(n - 1, 0, -1):
        if dp[i][capacity] != dp[i - 1][capacity]:
            selected_items[i] += 1
            capacity -= weights[i]

    if capacity >= weights[0]:
        selected_items[0] += capacity // weights[0]

    return selected_items

capacity = 14
weights = [4, 6, 8]
profits = [7, 6, 9]
n = len(profits)
dp = [[-1 for _ in range(capacity + 1)] for _ in range(n)]

start = timeit.default_timer()
print(f"Max Profits: {unboundedKnapsack(capacity, weights, profits, n - 1, dp, [0] * n)}")
end = timeit.default_timer()
print(f"Runtime was: {(end - start)*1000000} microseconds")
memory_usage = sys.getsizeof(dp)
print("Memory usage of array K: {} bytes".format(memory_usage))

selected_items = traceSelectedItems(capacity, weights, profits, dp)
print("Selected items: ", selected_items)
print(f"Total profit for Capacity {capacity}: {selected_items[0]}({profits[0]}) + {selected_items[1]}({profits[1]}) + {selected_items[2]}({profits[2]}) = {unboundedKnapsack(capacity, weights, profits, n - 1, dp, [0] * n)}")
#print(f"Total profit for Capacity {capacity}: {total_profit[0]} + {total_profit[1]} + {total_profit[2]} = {sum(total_profit)}")

