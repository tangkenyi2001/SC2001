import timeit
import tracemalloc
import sys

def knapsack_recur(C, n, w, p):
    if n == 0 or C == 0:
        return 0
    if w[n-1] > C:
        return knapsack_recur(C, n-1, w, p)
    else:
        return max(p[n-1] + knapsack_recur(C-w[n-1], n-1, w, p) , knapsack_recur(C, n-1, w, p))
    
def knapsack_recur_unbounded(C, n, w, p):
    if n == 0 or C == 0:
        return (C//w[0])*p[0]
    not_taken = 0 + knapsack_recur_unbounded(C, n-1, w, p)
    taken = -100
    if w[n] <= C:
        taken = p[n] + knapsack_recur_unbounded(C - w[n], n, w, p)
    return max(taken, not_taken)
    
if __name__ == "__main__":
    C = 14 # capcacity of knapsack
    w = [4, 6, 8,10,12]
    p = [7, 6, 9,11,11]
    n = len(p) # number of object
    start = timeit.default_timer()
    K = knapsack_recur_unbounded(C, n-1, w, p)
    end = timeit.default_timer()
    print(f"Max Profits: {K}")
    print("Runtime: {:.3f} microseconds".format((end - start)*1e6))
    memory_usage = sys.getsizeof(K)
    print("Memory Use: {} bytes".format(memory_usage))
