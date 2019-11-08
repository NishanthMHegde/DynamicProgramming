#Problem statement: There are N steps to climb to reach heaven. Find out in how many ways these N steps can be climbed to reach heaven. 
#You can either take 1 step or 2 steps at a time.

num_steps = 10
num_ways = list()
num_ways.append(1)
num_ways.append(1) #we cna climb one step in one way only

# number of ways of climbing each step is equal to number of ways of climbing (n-1) plus number of ways of climbing (n-2) steps

for i in range(2, num_steps+1):
	num_ways.append(num_ways[i-1] + num_ways[i-2])

print(num_ways)
print("Total number of ways of climbing %s number of steps is %s" % (num_steps), num_ways)
