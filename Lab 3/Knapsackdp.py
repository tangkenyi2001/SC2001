import timeit
import sys
import random

def max(i, j):
    return i if i > j else j

def knapSack(C, weight, value, n):
    K = [[0 for x in range(C + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for c in range(C + 1):
            if i == 0 or c == 0:
                K[i][c] = 0
            elif weight[i - 1] <= c:
                K[i][c] = max(value[i - 1] + K[i][c - weight[i - 1]], K[i - 1][c])
            else:
                K[i][c] = K[i - 1][c]

    return K

def traceSelectedItems(capacity, weights, K):
    n = len(weights)
    selected_items = [0] * n

    c = capacity
    i = n
    while i > 0 and c > 0:
        if K[i][c] != K[i - 1][c]:
            selected_items[i - 1] += 1
            c -= weights[i - 1]
        else:
            i -= 1

    return selected_items

capacity = 14
min_weight = 1
max_weight = 20
min_profit = 5
max_profit = 15

# Generate random weights and profits for 100 elements
weights = [random.randint(min_weight, max_weight) for _ in range(3)]
profits = [random.randint(min_profit, max_profit) for _ in range(3)]
n = len(profits)

start = timeit.default_timer()
K = knapSack(capacity, weights, profits, n)
end = timeit.default_timer()
max_profit = K[n][capacity]


print(f"Max Profits: {max_profit}")
print("Runtime: {:.3f} microseconds".format((end - start)*1e6))
memory_usage = sys.getsizeof(K)
print("Memory Use: {} bytes".format(memory_usage))

selected_items = traceSelectedItems(capacity, weights, K)
print("Selected items: ", selected_items)
print(f"Total profit for Capacity {capacity}: {selected_items[0]}({profits[0]}) + {selected_items[1]}({profits[1]}) + {selected_items[2]}({profits[2]}) = {max_profit}")

#print("Finished 2D DP Array:")
#for row in K:
    #print(row)
