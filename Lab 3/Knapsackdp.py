# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 


def knapSack(C, wt, val, n): 
    K=[[]*C for _ in range(n+1)]
    for i in range(C):
        K[0][i]=0
    for i in range(n+1):
        K[i][0]=0
	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(C): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] 
							+ K[i-1][w-wt[i-1]], 
							K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 

	return K[n][W] 


# Driver code 
if __name__ == '__main__': 
	profit = [7, 6, 9] 
	weight = [5, 6, 8] 
	C = 14
	n = len(profit) 
	print(knapSack(C, weight, profit, n)) 

