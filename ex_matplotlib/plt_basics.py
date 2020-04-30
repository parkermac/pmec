"""
Code to test various aspects of matplotlib for making plots.

"""

# imports
import sys, os
import numpy as np
import matplotlib.pyplot as plt

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod

# make sure the output directory exists
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
mymod.make_dir(out_dir)

# make some lines to plot
x = np.linspace(0, 10, 500)
y = np.sin(x**2)

# plotting
plt.close('all')
fig = plt.figure(figsize=(12,8))

ax = fig.add_subplot(111)
ax.plot(x, y, '-g', linewidth=3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(0,10)
ax.grid(True)

plt.show()
