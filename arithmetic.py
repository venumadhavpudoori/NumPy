import numpy as np

# Create sample arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Addition
print("Addition:", arr1 + arr2)
#output: Addition: [11 22 33 44 55]

# Subtraction
print("Subtraction:", arr1 - arr2)
#output: Subtraction: [-9 -18 -27 -36 -45]

# Multiplication
print("Multiplication:", arr1 * arr2)
#output: Multiplication: [10 40 90 160 250]

# Division
print("Division:", arr2 / arr1)
#output: Division: [10. 10. 10. 10. 10.]

# Power
print("Power:", arr1 ** 2)
#output: Power: [ 1  4  9 16 25]


# Element-wise operations
print("Square root:", np.sqrt(arr1))
#output: Square root: [1. 1.41421356 1.73205081 2. 2.23606798]
print("Absolute value:", np.abs(arr1 - arr2))
#output: Absolute value: [9 18 27 36 45]

# 2D array operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("\nMatrix Addition:\n", matrix1 + matrix2)
#output:
#Matrix Addition:   [[ 6  8]
#                   [10 12]]    

print("\nMatrix Multiplication (element-wise):\n", matrix1 * matrix2)
#output:
#Matrix Multiplication (element-wise):   [[ 5 12]   
#                                         [21 32]]

print("\nMatrix Dot Product:\n", np.dot(matrix1, matrix2))
#output:
#Matrix Dot Product:   [[19 22]
#                       [43 50]]
