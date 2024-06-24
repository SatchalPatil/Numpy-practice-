# copy and view array
# copy makes a separate object of the existing object such that if any changes are made
# in existing object the copied object remains unchanged
# this is completely opposite for view function

import numpy as np

arr = np.array([1,2,3,4,5,6,7])

cpy = np.copy(arr)

vw = arr.view()

arr[0] = 12

print(cpy)
print(vw)

