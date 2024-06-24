# poisson distribution estimates how many times a event may occur
# parameters : lam : number or rate of occurence , size 

# model NO. of sign ups on a website 
# if avg signup per hour is 4

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.poisson(lam=4,size = 10)
print(arr)

sns.distplot( random.poisson(lam=4,size = 1000),hist = False)
plt.show()