"""
This is a typical way to format a program.
"""

# always do imports first
import numpy as np
import matplotlib.pyplot as plt

# now make some variables
x =np.linspace(0,10,100)
y = x**2

# here is an if statement
if len(x) > 50:
    print('hello')

# plotting to the screen

# first get rid of old figures
plt.close('all')

# initialize a figure object
fig = plt.figure(figsize=(8,8))

# initialize an axis object
ax = fig.add_subplot(111)

# use the "plot" method of the ax object
ax.plot(x, y, '--g', linewidth=3)

# and make sure it shows up
plt.show()
