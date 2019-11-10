"""
Problem: Given an array of integers, find out the longest possible length of series where the numbers are in ascending order. The numbers can be consecutive or non-consecutive (sub-sequence).

Example:
Consider the below array:

10 13 11 20 37 80 50

In the above example, the longest increasing subsequence would be 10 13 20 37 80 which has a length of 5. 
"""


def find_lis(arr):
	LIS = list()
	longest_inc_subsequence = None 

	#initialize the LIS to 1 as the minimum lis is 1
	for i in range(len(arr)):
		LIS.append(1)

	#check if an increasing subsequence is found on each index. If found check the length of subsequence and then increment the LIS 
	#at each index
	for i in range(1, len(arr)):
		for j in range(0, i):
			if (arr[i] > arr[j]) and (LIS[i] < LIS[j] + 1):
				LIS[i] = LIS[i] + 1
			else:
				continue

	print("The LIS at each index is %s" % (LIS))
	print("The length of longest increasing subsequence is %s" %(max(LIS)))

arr = [10, 13, 11, 20, 37, 80, 50]
find_lis(arr)
arr = [15, 14, 13, 16, 54, 9, 21, 11]
find_lis(arr)
arr = [15, 14, 13, 16, 54, 9, 21, 11, 77]
find_lis(arr)
arr = [1, 2, 0, 3, -1, -100]
find_lis(arr)