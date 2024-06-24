# normal distribution , LOC(mean), scale(SD), Size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.normal(size = (2,3))
print(arr,"\n")

# parameterzed 

arr2 = random.normal(size = (3,4),loc=1,scale=2)
print(arr2)

sns.distplot( random.normal(size = 1000),hist=False)
plt.show()