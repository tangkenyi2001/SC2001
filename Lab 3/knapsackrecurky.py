import timeit
import sys
def max(i, j):
    return i if i > j else j

def knapSack(C, weight, value, n):
    if n == 0 or C == 0:
        return 0

    if weight[n - 1] > C:
        return knapSack(C, weight, value, n - 1)
    
    return max(value[n - 1] + knapSack(C - weight[n - 1], weight, value, n), knapSack(C, weight, value, n - 1))

if __name__ == "__main__":
    weights = [5, 6, 8] 
    profits = [7, 6, 9]
  
    C = 14
    n = len(weights)
    start = timeit.default_timer()
    K = knapSack(C, weights, profits, n)
    end = timeit.default_timer()
    print(f"Max Profits: {K}")
    print("Runtime: {:.3f} microseconds".format((end - start)*1e6))
    memory_usage = sys.getsizeof(K)
    print("Memory Use: {} bytes".format(memory_usage))
