# you can user arguments marker to emphsize each poitn point with specifed markers.
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Y

"""ypoint = np.array([3, 8 ,1, 10])
plt.plot(ypoint, marker = 'o')
plt.show()"""

#format strings (FMT)-marker| line |color 
"""ypoint = np.array([3, 8 ,1, 10])
plt.plot(ypoint, 's-.b')
plt.show()"""

# line Refernce 
# - solid line,   : dotted line, -- dashed line, -.dash and dotted line.
# Color Refernce
# r red, g green, b blue, c Cyan, m mgenta, y yellow, k black, w white.

# marker size, ms = marker size, mec = marker color, mfc =marker face color
ypoint = np.array([3, 8 ,1, 10])
plt.plot(ypoint, marker = 's', ms=20, mec = 'k', mfc ='hotpink')
plt.show()