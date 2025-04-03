from matplotlib import pyplot as plt
import numpy as np

mu, sigma=100, 15
x = mu+sigma*np.random.randn(10000)

fig,ax = plt.subplots()
ax.hist(x, bins=50,color="red")

fig.savefig("myPng.png")

plt.show()