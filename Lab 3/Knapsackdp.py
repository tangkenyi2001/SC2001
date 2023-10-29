# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 
import sys
import time
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                              + K[i-1][w-wt[i-1]], 
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    q = n
    a = W
    selected_items = []

    while q > 0 and a > 0:
        if K[q][a] != K[q-1][a]:
            selected_items.append(val[q-1])
            a -= wt[q-1]
        q -= 1

    # Reverse the selected items list to get the correct order
    selected_items.reverse()
    '''for row in K:
        for element in row:
            print(element, end=' ')  # Use end=' ' to print elements on the same line
        print()'''
    memory_usage = sys.getsizeof(K[0]*(n+1))
    print("Memory usage of 2D array K: {} bytes".format(memory_usage))
    
    return K[n][W], selected_items

# Driver code 
if __name__ == '__main__': 
	profit = [7, 6, 9] 
	weight = [5, 6, 8] 
	C = 14
	n = len(profit) 
start=time.time()
max_value, selected_items = knapSack(C, weight, profit, n)
end=time.time()
print("Profit:",profit)
print("Weight:",weight)
print("Time Taken:",end-start)
print("Maximum value:", max_value)
print("Selected items: Items that are worth ", selected_items)
