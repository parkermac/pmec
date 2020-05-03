"""
Code to test various aspects of matplotlib for making plots.

The emphasis here is on 2-D fields plotted as colors and contours.

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

# make a field to plot
N = 100
# box edges
X = np.linspace(-1,1,N+1)
Y = np.linspace(-1,1,N+1)
XX, YY = np.meshgrid(X,Y)
# box centers and data
x = X[:-1] + np.diff(X)/2
y = Y[:-1] + np.diff(Y)/2
xx, yy = np.meshgrid(x,y)
r = np.sqrt((xx-.25)**2 + (yy-.5)**2)
z = np.cos(8*r) + xx

# PLOTTING
plt.close('all')

# colormaps
fig = plt.figure(figsize=(18,6))
counter = 1
for cmap in ['viridis', 'Spectral']:
    ax = fig.add_subplot(1,2,counter)
    cs = ax.pcolormesh(XX, YY, z, cmap=cmap)
    fig.colorbar(cs)
    ax.axis('square')
    ax.set_title(cmap)
    counter += 1

# contours
fig = plt.figure(figsize=(18,6))

ax = fig.add_subplot(1,3,1)
cs = ax.contour(xx,yy,z, np.linspace(-1.5,1.5, 7), linewidths=2)
plt.clabel(cs)
ax.axis('square')
ax.set_title('Basic contours with labels')

ax = fig.add_subplot(1,3,2)
cs = ax.contour(xx,yy,z, np.linspace(-1.5,1.5, 7), linewidths=2, colors='b')
ax.axis('square')
ax.set_title('Basic contours with set color')

ax = fig.add_subplot(1,3,3)
ax.contour(xx,yy,z, 0, colors='m', linewidths=4, alpha=.5)
cs = ax.contour(xx,yy,z, [-1.5, -1.0, -.5], colors='g', linewidths=[1,3,5], linestyles='dotted')
plt.clabel(cs, fmt='%0.1f', fontsize=16)
cs = ax.contour(xx,yy,z, [.5, .8, 1.1],
    colors=['moccasin','darkorange','saddlebrown'], linewidths=4, linestyles='solid')
ax.axis('square')
ax.set_title('More control over contours')


plt.show()
