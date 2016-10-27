import random
import numpy as np
from matplotlib import pyplot as plt

mu, sigma = 1, 2
s = np.random.normal(mu, sigma, 10000)

n, bins, patches = plt.hist(s, 100, normed=True)

plt.xlabel('Smarts')
plt.ylabel('Problbility')
plt.title('Histogram of IQ')
plt.text(-2, .2, r'$\mu=1,\ \ sigma=2$')
plt.grid(True)

plt.show()
