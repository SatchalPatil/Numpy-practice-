# array shaping

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
 
print(arr.shape)

arr = np.array([[1,2,3,4],[5,6,7,8]], ndmin=5)
print(arr)
print(arr.shape)