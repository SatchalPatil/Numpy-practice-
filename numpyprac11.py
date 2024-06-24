# Binomial Distribution
# n = no. of trials, p = probablity , size=shape

# PS trial for a coin flipped 10 times

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.binomial(n=10 , p=0.5 , size = 10 )
print(arr)

# visualization

sns.distplot(random.binomial(n=10 , p=0.5 , size = 1000) , hist = True  )
plt.show()