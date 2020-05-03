"""
Code to test various aspects of matplotlib for making plots.

The emphasis here is on line plots, and the arrangement of multiple plots.

"""

# imports
import sys, os
import numpy as np
import matplotlib.pyplot as plt

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
# make sure the output directory exists
this_parent, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir) 

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

tstr = 'A minimal plot'
#
# You could do this more quickly as plt.plot(x,y1) but I always
# make separate figure (fig) and axis (ax) objects since all non-trivial plots
# benefit from being able to access the methods for these directly.
fig = plt.figure()
ax = fig.add_subplot(111) # (111) is shorthand for (1,1,1)
ax.plot(x, y1)
ax.set_title(tstr)
# saving as a png
fig.savefig(out_dir + 'minimal_plot.png')

tstr = 'Four lines on one plot, with a legend'
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
for aa in abc_list:
    ax.plot(x, y_dict[aa], label=aa)
ax.set_title(tstr)
ax.legend(fontsize=20, ncol=2)
# use help(ax.legend) to find info on arguments you can pass,
# like fontsize, or number of columns

# Note that I can keep remaking the fig and ax objects, which refer to new
# things each time.  You could also give them specific names like fig1 and ax1
# if you wanted to keep working on them.

tstr = 'Four plots in a grid, using y_dict to make it a for-loop'
# this is a quick way to cycle through a number of plots
fig = plt.figure(figsize=(12,8)) # set the figure size (width, height)
counter = 1
for aa in abc_list:
    ax = fig.add_subplot(2,2,counter)
    # the add_subplot() method accepts (nrows, ncols, naxis)
    # where naxis starts one and advances along each row:
    # 1 2
    # 3 4
    # like in MATLAB
    ax.plot(x, y_dict[aa])
    ax.set_title(aa)
    counter += 1
fig.suptitle(tstr) # add a title over all the plots

tstr = 'Four plots in a grid, using subplots array'
# this might be useful if the plotting is organized by row or column
NR = 2; NC = 2
fig, axes = plt.subplots(nrows=NR, ncols=NC, figsize=(12,8), squeeze=False)
axes[0,0].plot(x,y1)
axes[0,1].plot(x,y2)
axes[1,0].plot(x,y3)
axes[1,1].plot(x,y4)
fig.suptitle(tstr) # add a title over all the plots

tstr = 'Mix and match grids of subplots'
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(2,2,1)
ax.plot(x, y1)
ax = fig.add_subplot(2,2,3)
ax.plot(x, y2)
ax = fig.add_subplot(1,2,2)
ax.plot(x, y3)
fig.suptitle(tstr)

tstr = 'More flexible axes widths in a grid using subplot2grid()'
fig = plt.figure(figsize=(12,8))
# make axes that cover the left 2/3rds of the figure
ax = plt.subplot2grid((3,3), (0,0), colspan=2)
# the first tuple is (nrows, ncols)
# the second tuple is the index (row, col) starting from 0
# colspan gives how many columns (of 3) are spanned by this axis
ax.plot(x, y1)
ax = plt.subplot2grid((3,3), (1,0), colspan=2)
ax.plot(x, y2)
ax = plt.subplot2grid((3,3), (2,0), colspan=3)
ax.plot(x, y3)
ax = plt.subplot2grid((3,3), (0,2), rowspan=2)
ax.plot(x, y4)
fig.suptitle(tstr)

tstr = 'Twin axes'
fs = 16
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax.plot(x, y1,'-r')
ax.set_ylabel('y1', color='r', size=fs)
ax2 = ax.twinx()
ax2.plot(x, y2,'-b')
ax2.set_ylabel('y2', color='b', size=fs)
ax.set_title(tstr)

tstr = 'Fill above and below'
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax.fill_between(x, y1, where=(y1>0), color='r')
ax.fill_between(x, y1, where=(y1<0), color='b')
ax.set_title(tstr)

# show all figures on the screen
plt.show()
