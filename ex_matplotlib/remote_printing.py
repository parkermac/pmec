"""
A test of auto-detect of the environment to assist with plotting.
What it does is to see if you are on your laptop
- in which case it makes a screen plot,
or if you are on fjord
- in which case it saves the figure as a .png without showing
it on the screen.

IMPORTANT:

** On fjord: run from ipython, NOT ipython --pylab

The reason is that when you do "--pylab" it sets the graphical backend,
and for some reason the default on remote machines is not what we
want for saving plots.

In general when you work on the remote machine you ONLY save plots.

"""
# imports
import sys, os
import numpy as np

# this is the switch to sense what machine you are on automatically,
# and then make suitable plotting choices
host = os.getenv('HOSTNAME')
if host == None:
    # I'm unsure about the best test to use here.  This works on my mac
    # but I have no idea about other machines.  One could also try other
    # environmant variables like 'HOME' or 'USER' but these would have
    # to be edited for each person. 
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
cs = ax.pcolormesh(XX, YY, z)
fig.colorbar(cs)
ax.axis('square')

if save_fig:
    fig.savefig(out_dir + 'remote_printing.png')
else:
    plt.show()