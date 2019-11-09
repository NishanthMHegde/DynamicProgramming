"""#Problem: you are given a rod of length N inches and an array of size N+1 where the ith item represents the cost for ith inch of the rod.
Consider an example rod of length 4 inches and array:
0 2 4 5 7
"""

#In this example we are given 4 inch rod. Find max profit to be earned.
rod_cost = [0, 2 ,4 ,5, 7]
size = len(rod_cost)

#array which contains max profit for each inch of rod
rod = list()
rod.append(0)

for i in range(1, size):
	max_profit = -999999999
	for j in range(1, i+1):
		max_profit = max(max_profit, rod_cost[j] + rod[i-j])
	rod.append(max_profit)


print(rod)
