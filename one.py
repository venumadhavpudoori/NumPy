import numpy as np

# Create a 1D array dynamically from a list
n = int(input("Enter the size of the array: "))
arr = np.ndarray(shape=(n), dtype=int)

print("enter:", n)
for i in range(n):
    arr[i] = int(input())

print("arr:", arr)