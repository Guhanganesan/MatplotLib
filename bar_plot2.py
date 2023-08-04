import matplotlib.pyplot as plt
import numpy as np

x = np.array([3, 8, 1, 10])
y = np.array(["A", "B", "C", "D"])

plt.barh(x,y, height=0)
plt.show()