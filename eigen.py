import numpy as np

# Create a sample square matrix
A = np.array([[4, -2],
              [1, 1]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
#output: Eigenvalues:
# [3. 2.]


print("\nEigenvectors:")
print(eigenvectors)
#output: Eigenvectors:
# [[ 0.89442719  0.70710678]
#  [ 0.4472136  -0.70710678]]


# Access individual eigenvalue and eigenvector
print("\nFirst eigenvalue:", eigenvalues[0])
#output: First eigenvalue: 3.0

print("First eigenvector:", eigenvectors[:, 0])
#output: First eigenvector: [0.89442719 0.4472136 ]

# Verify: A @ v = λ @ v
v = eigenvectors[:, 0]
lam = eigenvalues[0]
print("\nVerification:")
print("A @ v =", A @ v)
#output: A @ v = [2.68328157 1.34164079]

print("λ @ v =", lam * v)
#output: λ @ v = [2.68328157 1.34164079]