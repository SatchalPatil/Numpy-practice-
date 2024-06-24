# array slicing
import numpy as np

arr= np.array([1,2,3,4,5,6,7,8,9,10])

print("from 3rd ele to 8 ele in 1D")
print(arr[2:8])
print("from start ele to 4 ele in 1D")
print(arr[:5])
print("neg slicing from 4th ele to end ele in 1D")
print(arr[-6:])

# taking steps
print("every other number ")
print(arr[1::2])

# slicing 2D array
arr2= np.array([[1,2,3,4],[5,6,7,8]])
print("from 5 to 7 in 2D array")
print(arr2[1,0:3])


# slicing 3D array

arr3= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print("3D 7 to 9")
print(arr3[1,0,0:3])

print(" 1 2 4 5")
print(arr3[0,0:2,0:2])
