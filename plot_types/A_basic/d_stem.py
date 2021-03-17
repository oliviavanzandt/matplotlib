"""
=================
stem([x], y, ...)
=================
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('cheatsheet_gallery')

# make data
np.random.seed(3)
X = 0.5 + np.arange(8)
Y = np.random.uniform(2, 7, len(X))

# plot
fig, ax = plt.subplots()

ax.stem(X, Y, bottom=0, linefmt="-", markerfmt="d")

ax.set_xlim(0, 8)
ax.set_xticks(np.arange(1, 8))
ax.set_ylim(0, 8)
ax.set_yticks(np.arange(1, 8))
plt.show()
