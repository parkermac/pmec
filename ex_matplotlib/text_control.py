"""
Plotting tips focused on text.

LaTeX Good resource:
https://matplotlib.org/3.1.1/tutorials/text/mathtext.html
You should use raw strings (precede the quotes with an 'r')

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

# ----------------------------------------------------------------------

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pcolormesh(XX,YY, zc, cmap='Wistia')

ax.text(.05, .9, 'Always use \"transform = ax.transAxes\"', fontsize=fs, transform = ax.transAxes)

ax.text(.95, .8, 'Right Justified', fontsize=fs, transform = ax.transAxes, ha='right')

ax.text(.5, .7, 'Rotated -30', fontsize=fs, transform = ax.transAxes,
    ha='center', va='center', rotation=-30)

ax.text(.5, .5, r'LaTeX formatting: $\Delta\rho\ =\ 1.5\ [kg\ m^{-3}]$',
    fontsize=fs, ha='center', transform = ax.transAxes)

ax.text(.5, .4, 'Color, Style, and Weight', fontsize=fs, transform = ax.transAxes,
    style='italic', weight='bold', color='darkmagenta', ha='center')
    
ax.text(.5, .3, 'Bounding Box Loud', fontsize=fs, transform = ax.transAxes,
    ha='center', bbox=dict(facecolor='palegreen', edgecolor='b'))
    
h = ax.text(.5, .2, 'Bounding Box Subtle', fontsize=fs, transform = ax.transAxes,
    ha='center', bbox=dict(facecolor='w', edgecolor='None', alpha=0.5))
    
plt.show()

fig.savefig(out_dir + 'm2_text_control.png')

