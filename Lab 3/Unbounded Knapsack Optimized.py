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

def unboundedKnapsack_explained(W): 
    weights = [5, 6, 8]
    profits = [7, 6, 9]
  
    dp = [0 for i in range(W + 1)] 
    quantities = [[0] * len(profits) for _ in range(W + 1)]  # Initialize quantities array

    for i in range(W + 1): # Iterate over all capacities from 0 to [W + 1]
        for j in range(len(profits)): # Iterate over all types of objects
            if (weights[j] <= i): # if the weight of the j-th item is less than or equal to the current capacity
               if dp[i - weights[j]] + profits[j] > dp[i]:
                    dp[i] = dp[i - weights[j]] + profits[j]
                    quantities[i] = quantities[i - weights[j]].copy()  # Copy quantities from the previous state
                    quantities[i][j] += 1  # Update quantity for the j-th item
    return dp[W], quantities[W]  # Return the maximum profit and the quantities of each item included in the optimal solution

weights = [5, 6, 8]
profits = [7, 6, 9]
total_profit = [0, 0, 0]
capacity = 14

start_time = timeit.default_timer()
max_profit = unboundedKnapsack(capacity)
end_time = timeit.default_timer()
print("\nMaximum profit:", max_profit)
print("Runtime: {:.3f} microseconds".format((end_time - start_time)*1e6))

memory_usage = sys.getsizeof(unboundedKnapsack(capacity))
print(f"Memory Use: {memory_usage} bytes")

start_time = timeit.default_timer()
max_profit, optimal_items = unboundedKnapsack_explained(capacity)
end_time = timeit.default_timer()
print("Maximum profit:", max_profit)
print("Time taken: {:.12f} seconds".format(end_time - start_time))

memory_usage = sys.getsizeof(unboundedKnapsack_explained(capacity))
print(f"Memory Usage: {memory_usage} bytes")

print("Maximum profit:", max_profit)
for j in range(len(optimal_items)):
    print(f"Item {j + 1} [Weight: {weights[j]}, Unit Profit: {profits[j]}] {optimal_items[j]} units")

print(f"Total profit for Capacity {capacity}: ", end="")
for j in range(len(optimal_items)):
    total_profit[j] = profits[j] * optimal_items[j]
    print(f"{optimal_items[j]}({profits[j]})", end="")
    if j < len(optimal_items) - 1:
        print(" + ", end="")
print("\r")
print(f"Total profit for Capacity {capacity}: {total_profit[0]} + {total_profit[1]} + {total_profit[2]} = {sum(total_profit)}")
