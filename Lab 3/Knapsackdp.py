def unboundedKnapsack(c, w, p, idx, dp): 
    # Base Case 
    # if we are at idx 0. 
    if idx == 0: 
        return (c // w[0]) * p[0] 
    # If the value is already calculated then we will 
    # previous calculated value 
    if dp[idx][c] != -1: 
        return dp[idx][c] 
    # There are two cases either take element or not take. 
    # If not take then 
    notTake = 0 + unboundedKnapsack(c, w, p, idx - 1, dp) 
    # if take then weight = W-wt[idx] and index will remain 
    # same. 
    take = float('-inf') 
    if w[idx] <= c: 
        take = p[idx] + unboundedKnapsack(c - w[idx], w, p, idx, dp) 
    dp[idx][c] = max(take, notTake) 
    return dp[idx][c] 
  
# Driver code 
capacity = 14
weights = [5, 6, 8]
profits = [7, 6, 9] 
n = len(profits) 
dp = [[-1 for _ in range(capacity+1)] for _ in range(n)] 
print(unboundedKnapsack(capacity, weights, profits, n-1, dp)) 