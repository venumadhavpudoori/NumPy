import numpy as np

# 1. array() - Create array from a list
arr_from_list = np.array([1, 2, 3, 4, 5])
print("array():", arr_from_list)

# 2. zeros() - Create array filled with zeros
zeros_1d = np.zeros(5)
zeros_2d = np.zeros((3, 4))
print("zeros() 1D:", zeros_1d)
print("zeros() 2D:\n", zeros_2d)

# 3. ones() - Create array filled with ones
ones_1d = np.ones(5)
ones_2d = np.ones((2, 3))
print("ones() 1D:", ones_1d)
print("ones() 2D:\n", ones_2d)

# 4. arange() - Create array with evenly spaced values (like range())
arange_basic = np.arange(0, 10)
arange_step = np.arange(0, 10, 2)
print("arange() basic:", arange_basic)
print("arange() with step:", arange_step)

# 5. linspace() - Create array with specified number of evenly spaced values
linspace_10 = np.linspace(0, 10, 5)
linspace_100 = np.linspace(0, 100, 11)
print("linspace() 0-10 (5 values):", linspace_10)
print("linspace() 0-100 (11 values):", linspace_100)

# 6. random() - Create array with random values
random_1d = np.random.random(5)
random_2d = np.random.random((3, 3))
random_int = np.random.randint(1, 10, 5)
print("random() 1D:", random_1d)
print("random() 2D:\n", random_2d)
print("random integers 1-9:", random_int)

# 7. eye() - Create identity matrix
identity_3x3 = np.eye(3)
identity_5x5 = np.eye(5)
print("identity matrix 3x3:\n", identity_3x3)
print("identity matrix 5x5:\n", identity_5x5)

