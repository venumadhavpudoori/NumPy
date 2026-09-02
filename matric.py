import numpy as np

# Create a 4x5 matrix
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print("Original matrix:")
print(matrix)

# Slice: first 2 rows, all columns
print("\nFirst 2 rows:")
print(matrix[0:2, :])

# Slice: all rows, first 3 columns
print("\nFirst 3 columns:")
print(matrix[:, 0:3])

# Slice: rows 1-3, columns 1-4
print("\nRows 1-3, columns 1-4:")
print(matrix[1:3, 1:4])

# Slice: every other row and column
print("\nEvery other row and column:")
print(matrix[::2, ::2])

# Slice: last row
print("\nLast row:")
print(matrix[-1, :])