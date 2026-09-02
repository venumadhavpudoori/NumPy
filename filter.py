import numpy as np

# Create sample array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 1. Boolean indexing (basic filtering)
filtered = arr[arr > 5]
print(filtered)  # [6 7 8 9 10]

# 2. Multiple conditions
filtered = arr[(arr > 3) & (arr < 8)]
print(filtered)  # [4 5 6 7]

# 3. Using np.where for conditional selection
filtered = np.where(arr > 5, arr, 0)
print(filtered)  # [0 0 0 0 0 6 7 8 9 10]

# 4. Using np.extract
filtered = np.extract(arr % 2 == 0, arr)
print(filtered)  # [2 4 6 8 10]

# 5. Combining with functional operations
result = arr[arr > 5].sum()
print(result)  # 40

# 6. Filter with custom function using np.vectorize
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

vfunc = np.vectorize(is_prime)
filtered = arr[vfunc(arr)]
print(filtered)  # [2 3 5 7]

# 7. Chain multiple filters
result = arr[(arr > 2) & (arr < 9)][::2]
print(result)  # [3 5 7]

# 8. Using np.isin for membership filtering
values = np.array([2, 4, 6, 8])
filtered = arr[np.isin(arr, values)]
print(filtered)  # [2 4 6 8]