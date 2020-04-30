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
from importlib import reload
reload(mymod)

# use a method in my_module to get the path to the output directory
this_parent, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir) # make sure the output directory exists

# make some lines to plot
x = np.linspace(0, 10, 500)
y1 = np.sin(x**2)
y2 = np.sqrt(x)
y3 = .3*(x - 5)**2 - 2
y4 = np.tanh(x)

# make a dict that associates letters with lines
abc_list = list('abcd') # a quick way to make the list ['a', 'b', 'c', 'd']
y_list = [y1, y2, y3, y4]
y_dict = dict(zip(abc_list, y_list))

# PLOTTING
plt.close('all') # always start by cleaning up

# 1. A minimal plot
#
# You could do this more quickly as plt.plot(x,y1) but I always
# make separate figure (fig) and axis (ax) objects since all non-trivial plots
# benefit from being able to access the methods for these directly.
fig = plt.figure()
ax = fig.add_subplot(111) # (111) is shorthand for (1,1,1)
ax.plot(x, y1)
ax.set_title('A minimal plot')

# 2. Four plots in a grid, using y_dict to make it a for loop
fig = plt.figure(figsize=(12,8)) # set the figure size (width, height)
counter = 1
for aa in abc_list:
    ax = fig.add_subplot(2,2,counter)
    # the add_subplot method accepts (number of rows, number of arguments,
    # and the number of this axis object counting from one and advancing along each row):
    # 1 2
    # 3 4
    ax.plot(x, y_dict[aa])
    ax.set_title(aa)
    counter += 1
# Note that I can keep remaking the fig and ax objects, which refer to new
# things each time.  You could also give them specific names like fig1 and ax1
# if you wanted to keep working on them.
    
# 3. Four lines on one plot, with a legend
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
for aa in abc_list:
    ax.plot(x, y_dict[aa], label=aa)
    ax.set_title('Use a legend')
ax.legend(fontsize=20, ncol=2)
# use help(ax.legend) to find info on arguments you can pass,
# like fontsize, or number of columns


# show all figures on the screen
plt.show()
