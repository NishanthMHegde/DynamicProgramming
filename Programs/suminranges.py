"""
Problem: Find the sum of all the numbers within a given range(inclusive) for a given array.
Given array,

2 5 4 1 6 8 4

sum_of_ranges(2, 6) = 23
sum_of_ranges(3, 5) = 15
"""

def sum_in_range(arr, i, j):
	sum = None
	sum_of_nums = list()
	sum_of_nums.append(arr[0])
	for k in range(1, len(arr)):
		sum_of_nums.append(arr[k] + sum_of_nums[k-1])
	print("Sum of nums array is %s" %(sum_of_nums))
	if i ==0:
		sum = sum_of_nums[j]
	else:
		sum = sum_of_nums[j] - sum_of_nums[i-1]
	print("The sum in range for i=%s and j=%s is %s" % (i, j, sum))



arr = [2, 5, 4, 1, 6, 8, 4]
print("Original array is %s"%(arr))
sum_in_range(arr, 2, 5)
sum_in_range(arr, 2, 6)
sum_in_range(arr, 0, 3)