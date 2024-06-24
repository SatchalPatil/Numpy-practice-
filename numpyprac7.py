# iterating array elements 

import numpy as np

arr= np.array([1,2,3,4,5,6,7,8,9,10])

for i in arr:
    print(i,"\n")

###############2D
arr2= np.array([[1,2,3],[4,5,6]])

for i in arr2:
    for j in i:
        print(j,"\n")

###############3D
arr3= np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,10,11]]])

for i in arr3:
    for j in i:
        for k in j:
            print(k,"\n")

# nditer funcn

arr3= np.array([[[1,2,3],[4,5,6]],[[6,7,8],[9,10,11]]])

for i in np.nditer(arr3):
    print(i)

for i in np.nditer(arr3[:,:,::3]):
    print(i)


