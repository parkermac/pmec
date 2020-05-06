"""
Plotting tips focused on map fields, inclusing inset colorbars.

"""

# imports
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import pickle

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
this_parent, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir) 

# load data to plot
in_dir = '../../' + this_parent + '_data/'
[salt,lon_psi,lat_psi] = pickle.load(open(in_dir + 'salt.p', 'rb'))
# note these are "masked arrays"

def dar(ax):
    """
    Fixes the plot aspect ratio to be locally Cartesian.
    """
    yl = ax.get_ylim()
    yav = (yl[0] + yl[1])/2
    ax.set_aspect(1/np.sin(np.pi*yav/180))

# PLOTTING
fs = 18 # primary fontsize
fs2 = 0.8*fs
plt.close('all')

fig = plt.figure(figsize=(20,12))

ax = fig.add_subplot(131)
# main plot
cs = ax.pcolormesh(lon_psi, lat_psi, salt, cmap='Spectral_r', vmin=28.4, vmax=34)
ax.set_title('(a) Surface Salinity', size=fs, weight='bold')
ax.set_xlabel('Longitude', size=fs)
ax.set_ylabel('Latitude', size=fs)
ax.tick_params(labelsize=fs2)
# Inset colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
cbaxes = inset_axes(ax, width="4%", height="40%", loc='lower right', borderpad=3) 
cb = fig.colorbar(cs, cax=cbaxes, orientation='vertical')
cb.ax.tick_params(labelsize=fs2)
# fix aspect ratio
dar(ax)

ax = fig.add_subplot(132)
# main plot
cs = ax.pcolormesh(lon_psi, lat_psi, salt, cmap='Spectral_r', vmin=28.4, vmax=34)
ax.set_title('(b) Remove ticks & labels', size=fs, weight='bold')
ax.set_xlabel('Longitude', size=fs)
ax.set_ylabel('Latitude', size=fs)
# *** Remove ticklabels ***
ax.set_xticklabels([])
ax.set_yticklabels([])
# *** Remove ticks ***
ax.set_xticks([])
ax.set_yticks([])
# ********************
# Inset colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
cbaxes = inset_axes(ax, width="4%", height="40%", loc='lower right', borderpad=3) 
cb = fig.colorbar(cs, cax=cbaxes, orientation='vertical')
cb.ax.tick_params(labelsize=fs2)
# fix aspect ratio
dar(ax)

ax = fig.add_subplot(133)
# main plot
cs = ax.pcolormesh(lon_psi, lat_psi, salt, cmap='Spectral_r', vmin=28.4, vmax=34)
ax.set_title('(c) Remove axes', size=fs, weight='bold')
# ax.set_xlabel('Longitude', size=fs)
# ax.set_ylabel('Latitude', size=fs)
# *** Remove axes ***
ax.set_axis_off()
# ********************
# Inset colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
cbaxes = inset_axes(ax, width="4%", height="40%", loc='lower right', borderpad=3) 
cb = fig.colorbar(cs, cax=cbaxes, orientation='vertical')
cb.ax.tick_params(labelsize=fs2)
# fix aspect ratio
dar(ax)

fig.savefig(out_dir + 'salt.png')

plt.show()

