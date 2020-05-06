"""
Plotting tips focused on colormaps.

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

# make a field to plot
N = 100
# box edges
X = np.linspace(-1,1,N+1)
Y = np.linspace(-1,1,N+1)
XX, YY = np.meshgrid(X,Y)
# box centers and data
xc = X[:-1] + np.diff(X)/2
yc = Y[:-1] + np.diff(Y)/2
xxc, yyc = np.meshgrid(xc,yc)
rc = np.sqrt((xxc-.25)**2 + (yyc-.5)**2)
zc = np.cos(8*rc) + xxc

# PLOTTING
fs = 24 # primary fontsize
lw = 3 # primary linewidth
plt.close('all')

fig = plt.figure(figsize=(12,10))

# ----------------------------------------------------------------------

cmap='Spectral'
ax = fig.add_subplot(221)
cs = ax.pcolormesh(XX,YY, zc, cmap=cmap)
ax.set_axis_off()
ax.axis('square')
fig.colorbar(cs)
ax.set_title(cmap, weight='bold')

# ----------------------------------------------------------------------

cmap='Spectral_r'
ax = fig.add_subplot(222)
cs = ax.pcolormesh(XX,YY, zc, cmap=cmap)
ax.set_axis_off()
ax.axis('square')
fig.colorbar(cs)
ax.set_title(cmap, weight='bold')

# ----------------------------------------------------------------------

from matplotlib import colors
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# Here we make a colormap from a list of colors:
cmap1 = LinearSegmentedColormap.from_list('From Scratch',['r','b',(0,0,0),'m'])
# The first argument 'From Scratch' is the name assigned to the colormap object
# and it is returned by cmap1.name.
# The second argument is a list of color names or (R,B,G) triple,
# (or R,B,G,A) where A is for "alpha" meaning transparency, a float between 0 and 1
# where 0 = transparent and 1 = opaque (full strength).
# By default the cmap object has 256 color steps, and you can see the (R,G,B,A)
# of each one by passing a number (0-255) as an argument:
# cmap(10) => (0.8823529411764706, 0.0, 0.11764705882352941, 1.0)

# You can use the colors module get more info on RGB values, e.g.
# colors.to_rgb('b') gives the RGB triple for blue: (0.0, 0.0, 1.0)

ax = fig.add_subplot(223)
cs = ax.pcolormesh(XX,YY, zc, cmap=cmap1)
ax.set_axis_off()
ax.axis('square')
fig.colorbar(cs)
ax.set_title(cmap1.name, weight='bold')

# ----------------------------------------------------------------------

# Here we make a colormap by concatenating two colormaps:
top = cm.get_cmap('Blues', 128)
bottom = cm.get_cmap('rainbow', 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
cmap2 = ListedColormap(newcolors, name='Concatenated')
# Note: this call top(np.linspace(0, 1, 128))
# returns a numpy array of RGBA with shape (128,4)

ax = fig.add_subplot(224)
cs = ax.pcolormesh(XX,YY, zc, cmap=cmap2)
ax.set_axis_off()
ax.axis('square')
fig.colorbar(cs)
ax.set_title(cmap2.name, weight='bold')

# ----------------------------------------------------------------------

fig.savefig(out_dir + 'm2_colormaps.png')

plt.show()