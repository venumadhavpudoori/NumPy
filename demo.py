import numpy as np

# Create a simple array
arr = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

# Print the array
print(arr)

# Array properties
print(f"Shape we called it tuple: {arr.shape}")
print(f"Data type: {arr.dtype}")
print(f"Size: {arr.size}")

# Create array with range
arr2 = np.arange(0, 10, 2)
print(arr2)

# Create array of zeros
arr3 = np.zeros(5)
print(arr3)

# Create array of ones
arr4 = np.ones(5)
print(arr4)