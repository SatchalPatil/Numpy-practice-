#array reshaping

import numpy as np

#1D to 2D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr2 = arr.reshape(6,2)
print(arr2)

#1D to 3D
arr3=arr.reshape(3,2,2)
print(arr3)

#3D to 1D
arr3= np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,10,11]]])
arr4 = arr3.reshape(-1)

print(arr4)