import matplotlib.pyplot as plt 
"""now pyplot package cab be reffered as plt"""
import numpy as np
"""now pyplot package cab be reffered as plt"""
# ploting x and y
# plot() functionis used to draw point or markers in a diagram.

xpoint = np.array([1,8])
ypoint = np.array([3,10])
plt.plot(xpoint,ypoint)

#plt.show() # comment out just for test.

# Plotting wihtout line
xpoint = np.array([1,8])
ypoint = np.array([3,10])
plt.plot(xpoint,ypoint,'o')

#plt.show() # comment out just for test.

# Plot differnt
xpoint = np.array([1,2,6, 8])
ypoint = np.array([3,8, 1,10])
plt.plot(xpoint,ypoint)

plt.show() 

# default x -point

# Plot differnt
ypoint = np.array([3, 8, 1,10,5, 7])

plt.plot(ypoint)

plt.show() 
