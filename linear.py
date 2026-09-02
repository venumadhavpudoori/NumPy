import numpy as np

# Create sample matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Determinant
det_A = np.linalg.det(A)
print(f"Determinant of A: {det_A}")
#output: Determinant of A: -2.0000000000000004

# Inverse
inv_A = np.linalg.inv(A)
print(f"Inverse of A:\n{inv_A}")
#output: Inverse of A:  
# [[-2.   1. ]
#  [ 1.5 -0.5]]


# Matrix multiplication
result = np.dot(A, B)  # or use A @ B
print(f"A @ B:\n{result}")
#output: A @ B:
# [[19 22]
#  [43 50]]


# Verify: A @ A^(-1) should be identity
identity = np.dot(A, inv_A)
print(f"A @ A^(-1) (should be identity):\n{identity}")
#output: A @ A^(-1) (should be identity):
# [[1. 0.]
#  [0. 1.]]
