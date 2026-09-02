import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = np.array(my_list)

print(f"Shape we called it tuple: {arr}")
print(f"Data type: {arr.dtype}")
print(f"Size: {arr.size}")
print(f"Dimensions: {arr.ndim}")


res = arr.reshape(3, 3)
print(res)
print(f"Dimensions: {res.ndim}")