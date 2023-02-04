import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

np.random.seed(0)
plt.style.use('ggplot')

nD = 200 # Dataset Size

X = np.random.uniform(-2, +2, (nD, 1))

Y = 2*X - 1 + np.random.normal(0, 0.3, (nD, 1))

# Visualizing Created Dataset
plt.scatter(X[:, 0], Y[:, 0], s=12)
plt.title('Created Dataset (y = 2x - 1 + e)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
