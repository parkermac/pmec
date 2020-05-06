"""
Plotting tips focused on fontsize, linewidth, and markers.

"""

# imports
import sys, os
import numpy as np
import matplotlib.pyplot as plt

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
this_parent, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir) 

# make some lines to plot
xs = np.linspace(0, 10, 500) # smooth line
ys = np.sin(xs**1.5)
xp = np.linspace(.2,9.8, 20) # discrete points
yp = np.sin(xp**1.5) + .1 * np.random.randn(len(xp))
# axis limits
x0 = xs[0]; x1 = xs[-1]
y0 = -1.5; y1 = 1.5

# PLOTTING
fs = 18 # primary fontsize
lw = 3 # primary linewidth
plt.close('all')

# ----------------------------------------------------------------------

tstr = ('Fontsizes, line widths, and markers')
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)
# lines
ax.plot(xs, ys, '-', color='darkorange', linewidth=lw, label='Smooth Line')
ax.plot(xp, yp, '*',
    markerfacecolor='y', markeredgecolor='b', markeredgewidth=2,
    markersize=24, label='Discrete Points')
# add a legend - this makes use of the labels we set for each line
# use lh? to get more info about choices you can make
lh = ax.legend(fontsize=fs, loc='lower left')
# axes limits, two versions
if False:
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
else:
    ax.axis([x0, x1, y0, y1])
# add grid lines
ax.grid(True)
# axis labels
ax.set_xlabel('X axis', fontsize=fs)
ax.set_ylabel('Y axis', fontsize=fs)
ax.tick_params(labelsize=.8*fs)
# title
ax.set_title(tstr, fontsize=1.2*fs, fontweight='bold', fontstyle='italic')

fig.savefig(out_dir + 'm2_fontsizes.png')

# ----------------------------------------------------------------------

tstr = ('Same, but using short kwargs')
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)
# lines
ax.plot(xs, ys, '-', color='darkorange', lw=lw, label='Smooth Line')
ax.plot(xp, yp, '*',
    mfc='y', mec='b', mew=2,
    ms=24, label='Discrete Points')
ax.legend(fontsize=fs, loc='lower left')
# axes limits, two versions
if False:
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
else:
    ax.axis([x0, x1, y0, y1])
# add grid lines
ax.grid(True)
# axis labels
ax.set_xlabel('X axis', size=fs)
ax.set_ylabel('Y axis', size=fs)
ax.tick_params(labelsize=.8*fs)
# title
ax.set_title(tstr, size=1.2*fs, weight='bold', style='italic')

# ----------------------------------------------------------------------

# RC SETUP (plotting defaults)
# for more info see:
# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.rc.html
def set_rc(fs=20, lw=5, mks=50):
    fs_small = .7*fs
    lw_small = .5*lw
    plt.rc('xtick', labelsize=fs_small)
    plt.rc('ytick', labelsize=fs_small)
    plt.rc('xtick.major', size=10, pad=5, width=lw_small)
    plt.rc('ytick.major', size=10, pad=5, width=lw_small)
    plt.rc('axes', lw=lw_small)
    plt.rc('lines', lw=lw, markersize=mks)
    plt.rc('font', size=fs)
    plt.rc('grid', color='g', ls='-', lw=lw_small, alpha=.3)
set_rc()

tstr = ('Controlling things using defaults: plt.rc()')
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)
# lines
ax.plot(xs, ys, '-', color='darkorange', label='Smooth Line')
ax.plot(xp, yp, '*',
    markerfacecolor='y', markeredgecolor='b', markeredgewidth=2,
    label='Discrete Points')
# axes limits, two versions
if False:
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
else:
    ax.axis([x0, x1, y0, y1])
# add grid lines
ax.grid(True)
# axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
# title
ax.set_title(tstr)
# Restore defaults: if you don't do this then the next plot you make will have the same
# settings, even if it is from re-running this code, or running a new program.
plt.rcdefaults()

fig.savefig(out_dir + 'm2_using_defaults.png')

# ----------------------------------------------------------------------
    
plt.show()