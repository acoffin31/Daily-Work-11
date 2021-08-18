import matplotlib.pyplot as plt
import math

x = (1, 2, 3, 4, 5)
y = []
for xs in x:
    y.append(math.sin(xs))
plt.plot(x, y)
plt.show()
