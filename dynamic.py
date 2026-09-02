import numpy as np

m=int(input("Enter the size of row: "))
n=int(input("Enter the size of column: "))
arr = np.ndarray(shape=(m,n), dtype=int)

print("Enter %d elements of %d x %d array:" % (m*n, m, n))
for i in range(m):
    for j in range(n):
        arr[i][j] = int(input())


print("array", arr)

