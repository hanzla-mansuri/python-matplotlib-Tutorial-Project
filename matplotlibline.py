import matplotlib.pyplot as plt
import numpy as np
# "line style" or "ls" is used to change style
# line color - color or c ; 
# line width - line width lw;
"""ypoint = np.array([3, 8, 1, 10])
plt.plot(ypoint, ls = 'dashed', color = 'r',lw = 5)
plt.show()"""

# multiple line
xpoints =np.array([6, 2, 7, 11])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
