import numpy as np


arr = np.ndarray(shape=(3,3,3), dtype=int)
val=1
x=arr.shape[0]
y=arr.shape[1]
z=arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k]=val
            val+=1

print("array", arr)