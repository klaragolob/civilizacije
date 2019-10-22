from scipy.stats import reciprocal
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

a, b = 0.00623, 1.01
mean, var, skew, kurt = reciprocal.stats(a, b, moments='mvsk')

x = np.linspace(reciprocal.ppf(0.01, a, b),
                reciprocal.ppf(0.99, a, b), 100)
ax.plot(x, reciprocal.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='reciprocal pdf')

plt.show()