# uniform distribution
# para : a(lw bound=0.0), b(up.bound=1.0)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.uniform(size = (2,3))
print(arr)

sns.distplot(random.uniform(size = 1000),hist=False)
plt.show()