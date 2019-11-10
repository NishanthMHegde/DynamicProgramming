"""
Problem: you are given an array on N elements where the index i represents the day and the element at ith position represents the value of the stock at day i. Find out the maximum profit that can be earned by selling the stock. Note that a stock can be sold only after it is bought and it can be sold on the day it is bought or in a future day. 

Example:

Consider the below array: 


8 2 1 4 3 5

We need to find the maxium profit earned for those values.
"""

share_price = [8, 1, 2, 4, 6, 3]
max_profit = None
profits = list()
min_till_now = list()

#find the minimum price seen till that particular day
min_till_now.append(share_price[0])
for i in range(1, len(share_price)):
	min_till_now.append(min(share_price[i], min_till_now[i-1]))

print("The minimum till now array is %s" % (min_till_now))

#calculate the maximum profit attainable at each day
for i in range(len(share_price)):
	profits.append(share_price[i] - min_till_now[i])

print("The maximum profit array for each day is %s" % (profits))
max_profit = max(profits)
print("The maximum profit attainable in the trading period is %s" % (max_profit))