# Logistics distribution
# parameters = loc(mean) , scale(SD), size

# modeling the time it takes for customers to complete an online purchase. We know the average time is 30 minutes, and we want to model the variability around this average time.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


arr = random.logistic(loc = 30 , scale = 10, size = 10)
print(arr)

sns.distplot(random.logistic(loc = 30 , scale = 10, size = 10),hist=True,kde=False)
plt.show()

