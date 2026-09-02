import numpy as np

# Sample data
data = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

#Average
average_result = np.arange(1,10)
to= average_result.reshape(3,3)
#output: [[1 2 3]
#         [4 5 6]
#         [7 8 9]]


# Sum
sum_result = np.sum(data)
#output: 39


# Mean
mean_result = np.mean(data)
#output: 3.9

# Median
median_result = np.median(data,axis=0)
#output: 3.0

# Variance
var_result = np.var(data)
#output: 2.89

# Standard Deviation
std_result = np.std(data)
#output: 1.7

# Minimum
min_result = np.min(data)
#output: 1

# Maximum
max_result = np.max(data)
#output: 9

# Sort
sorted_data = np.sort(data)
#output: [1 1 2 3 3 4 5 5 6 9]

# Dot product
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_result = np.dot(vector1, vector2)
#output: 32

arr5= np.arange(10, 30)
arr6= arr5.reshape(4,5)
#output: [[10 11 12 13 14]
#         [15 16 17 18 19]
#         [20 21 22 23 24]
#         [25 26 27 28 29]]

np.dot(arr6,2)
#output: [[20 22 24 26 28]
#         [30 32 34 36 38]  
#        [40 42 44 46 48]
#        [50 52 54 56 58]]
# 

a1 = np.array([1, 2, 3, 4])
a2 = np.array([5, 6, 7, 8])
np.dot(a1, a2)
#output: 70

ad1= np.array([[1, 2], [3, 4]])
ad2= np.array([[5, 6], [7, 8]])
np.dot(ad1, ad2)
#output: [[19 22]
#         [43 50]]

sd= np.array([1, 2])
md= np.array([[5, 6], [7, 8]])
np.dot(sd, md)
#output: [19 22]

