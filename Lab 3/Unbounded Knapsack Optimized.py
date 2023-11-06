import sys
import timeit

def unboundedKnapsack(W): 
    weights = [5, 6, 8] 
    profits = [7, 6, 9]
  
    # Create memoization array
    dp = [0 for i in range(W + 1)] 

    # Iterate over all capacities from 0 to [W + 1]
    for i in range(W + 1): 
        # Iterate over all types of objects
        for j in range(len(profits)): 
            # if the weight of j-th item <= to current capacity
            if (weights[j] <= i): 
                # Update the maximum profit for the current capacity
                dp[i] = max(dp[i], dp[i - weights[j]] + profits[j]) 
    return dp[W]
total_profit = [0, 0, 0]
capacity = 14

start_time = timeit.default_timer()
max_profit = unboundedKnapsack(capacity)
end_time = timeit.default_timer()
print("\nMaximum profit:", max_profit)
print("Runtime: {:.3f} microseconds".format((end_time - start_time)*1e6))

memory_usage = sys.getsizeof(unboundedKnapsack(capacity))
print(f"Memory Use: {memory_usage} bytes")


'''print("Maximum profit:", max_profit)
for j in range(len(optimal_items)):
    print(f"Item {j + 1} [Weight: {weights[j]}, Unit Profit: {profits[j]}] {optimal_items[j]} units")

print(f"Total profit for Capacity {capacity}: ", end="")
for j in range(len(optimal_items)):
    total_profit[j] = profits[j] * optimal_items[j]
    print(f"{optimal_items[j]}({profits[j]})", end="")
    if j < len(optimal_items) - 1:
        print(" + ", end="")
print("\r")
print(f"Total profit for Capacity {capacity}: {total_profit[0]} + {total_profit[1]} + {total_profit[2]} = {sum(total_profit)}")'''
