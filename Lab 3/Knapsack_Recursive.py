import time

def knapsack_recur(C, n, w, p):
    if n == 0 or C == 0:
        return 0
    if w[n-1] > C:
        return knapsack_recur(C, n-1, w, p)
    else:
        return max(p[n-1] + knapsack_recur(C-w[n-1], n-1, w, p) , knapsack_recur(C, n-1, w, p))
    
if __name__ == "__main__":
    C = 14 # capcacity of knapsack
    w = [5, 6, 8]
    p = [7, 6, 9]
    n = len(p) # number of objects
    start = time.time()
    print(knapsack_recur(C, n, w, p))
    end = time.time()
    print(f"runtime was: {end-start}")
