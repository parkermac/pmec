"""
A test of auto-detect of the environment to assist with plotting.

On fjord: run from ipython, not ipython --pylab

"""
# imports
import sys, os
import numpy as np
host = os.getenv('HOSTNAME')
if host == None: 
    save_fig = False
    print('Printing to screen')
elif 'fjord' in host:
    print('Printing to file')
    import matplotlib as mpl
    mpl.use('Agg')
    save_fig = True
else:
    print('Do not know what to do!')
    sys.exit()
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
fig = plt.figure()
ax = fig.add_subplot(111)
cs = ax.pcolormesh(XX, YY, z, cmap='rainbow')
fig.colorbar(cs)
ax.axis('square')

if save_fig:
    fig.savefig(out_dir + 'remote_printing.png')
else:
    plt.show()