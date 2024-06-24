# array indexing

import numpy as np

arr= np.array([1,2,3,4,5,6,7,8,9,10])
arr2= np.array([[1,2,3],[4,5,6]])
arr3= np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,10,11]]])


print(arr,"\n")
print(arr2,"\n")
print(arr3,"\n")

# indexing for 2D array
print("2nd ele in first row of 2D")
print(arr2[0,1])

print("3nd ele in 2nd row of 2D")
print(arr2[1,2])

# indexing for 3D array

print("3rd ele for 2 row")
print(arr3[0,1,2])

print("2nd ele for 3 row")
print(arr3[1,0,1])



