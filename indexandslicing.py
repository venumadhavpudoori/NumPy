import numpy as np

# Create sample arrays
arr1d = np.array([10, 20, 30, 40, 50])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# ===== BASIC INDEXING =====
print("1D Array Indexing:")
print(arr1d[0])      # First element: 10
print(arr1d[-1])     # Last element: 50

print("\n2D Array Indexing:")
print(arr2d[0, 0])   # First row, first column: 1
print(arr2d[1, 2])   # Second row, third column: 6
print(arr2d[-1, -1]) # Last row, last column: 9

# ===== SLICING =====
print("\n1D Array Slicing:")
print(arr1d[1:4])    # Elements from index 1 to 3: [20 30 40]
print(arr1d[::2])    # Every 2nd element: [10 30 50]
print(arr1d[::-1])   # Reverse: [50 40 30 20 10]

print("\n2D Array Slicing:")
print(arr2d[0:2, 1:3])   # First 2 rows, columns 1-2
print(arr2d[:, 0])       # All rows, first column: [1 4 7]
print(arr2d[1, :])       # Second row, all columns: [4 5 6]

# ===== BOOLEAN INDEXING =====
print("\nBoolean Indexing:")
mask = arr1d > 25
print(arr1d[mask])   # Elements greater than 25: [30 40 50]

# ===== FANCY INDEXING =====
print("\nFancy Indexing:")
indices = [0, 2, 4]
print(arr1d[indices])  # Elements at indices 0, 2, 4: [10 30 50]