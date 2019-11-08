"""
Problem: Consider an M*N matrix or grid. You are present in the top left corner/ cell of the matrix and your home is present in the \
bottom right corner of the matrix. Find out the total number of ways that you can take to reach your home.
"""

n = 4
m = 3
print("We have an %s * %s matrix" % (n, m))

mat = [ [0 for i in range(m)]for i in range(n)]

print("Initial matrix %s" % (mat))

#The number of ways of reaching the house when on the rightmost column or when on the bottom most row is 1 as \
# we either travel down or we travel to the right.

for i in range(n):
	mat[i][m-1] = 1

for i in range(m):
	mat[n-1][i] = 1

#the total number of of ways of reaching home is equal to total number of ways of reaching home from one cell to the right \
#plus the total number of ways of reaching home from one cell bottom.

for i in range(n-2, -1, -1):
	for j in range(m-2, -1, -1):
		mat[i][j] = mat[i+1][j] + mat[i][j+1]

print("Final matrix %s" % (mat))
print("Total number of ways to reach home is %s"% (mat[0][0]))