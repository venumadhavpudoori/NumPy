import numpy as np

m=int(input("Enter the size of row: "))
n=int(input("Enter the size of column: "))
arr = np.ndarray(shape=(m,n), dtype=int)


print("size:", arr.size)
print("shape:", arr.shape)
print("dimension:", arr.ndim)
