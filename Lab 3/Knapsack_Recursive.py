import timeit
import tracemalloc

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
    not_taken = 0 + knapsack_recur(C, n-1, w, p)
    taken = -100
    if w[n] <= C:
        taken = p[n] + knapsack_recur(C - w[n], n, w, p)
    return max(taken, not_taken)
    
if __name__ == "__main__":
    C = 14 # capcacity of knapsack
    w = [5, 6, 8]
    p = [7, 6, 9]
    n = len(p) # number of objects
    start = timeit.default_timer()
    print(knapsack_recur_unbounded(C, n-1, w, p))
    end = timeit.default_timer()
    print(f"runtime: {(end-start) * 10**6:.3f} milliseconds")
    tracemalloc.start()
    q = knapsack_recur_unbounded(C, n-1, w, p)
    print(f"{tracemalloc.get_traced_memory()[1]} bytes")
    tracemalloc.stop()