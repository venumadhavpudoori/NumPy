import numpy as np

# Create sample arrays
arr = np.array([1, 2, 3, 4, 5, 6])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# RESHAPE - Change array dimensions
reshaped = np.reshape(arr, (2, 3))
# Output: [[1 2 3]
#          [4 5 6]]

reshaped.ndim  # Output: 2


# TRANSPOSE - Swap axes
transposed = np.transpose(arr2d,axes=(0,1))
# Output: [[1 2 3]
#          [4 5 6]]
# Or use .T
transposed = arr2d.T
# Output: [[1 4]
#          [2 5]
#          [3 6]]

transposed.shape  # Output: (3, 2)
# CONCATENATE - Join arrays along existing axis
arr_a = np.array([[1, 2, 3],[4, 5, 6]])
arr_b = np.array([[1, 2, 3],[4, 5, 6]])
concatenated = np.concatenate((arr_a, arr_b), axis=0)
concatenated
# Output: [[1 2 3]
#          [4 5 6]]

# SPLIT - Divide array into sub-arrays
split_result = np.split(arr, 2)
# Output: [array([1, 2, 3]), array([4, 5, 6])]

# STACK - Join arrays along new axis
stacked = np.stack((arr_a, arr_b), axis=0)
# Output: [[[1 2 3]
#           [4 5 6]]
stacked.ndim  # Output: 3

# VSTACK - Stack arrays vertically (row-wise)
vstacked = np.vstack([arr_a, arr_b])
# Output: [[1 2 3]
#          [4 5 6]]

# HSTACK - Stack arrays horizontally (column-wise)
hstacked = np.hstack([arr_a, arr_b])
# Output: [[1 2 3 1 2 3]
#          [4 5 6 4 5 6]]

vstacked.shape  # Output: (4, 3)
hstacked.shape  # Output: (2, 6)

# FLIP - Reverse array along axis
flipped = np.flip(arr2d)  # Flip all
#output: [[6 5 4]
#         [3 2 1]]

flipped_axis = np.flip(arr2d, axis=0)  # Flip rows
# Output: [[4 5 6]
#          [1 2 3]] 
flipped_axis = np.flip(arr2d, axis=1)  # Flip columns
# Output: [[3 2 1]
#          [6 5 4]]

# HSTACK - Stack arrays horizontally (column-wise)
hstacked = np.hstack([arr_a, arr_b])
# Output: [1 2 3 4 5 6]