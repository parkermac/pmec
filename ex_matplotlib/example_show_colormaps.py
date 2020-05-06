"""
Code to show off colormaps
"""

import numpy as np
import matplotlib.pyplot as plt

N = 200
X = np.linspace(-1,1,N+1)
Y = np.linspace(-1,1,N+1)
XX, YY = np.meshgrid(X,Y)
x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)
xx, yy = np.meshgrid(x,y)
r = np.sqrt((xx-.25)**2 + (yy-.5)**2)
z = np.cos(8*r) + xx

# get a list of available colormaps
cml = plt.colormaps()
# remove reversed one
cml = [item for item in cml if '_r' not in item]

# plotting
plt.close('all')

fig = plt.figure(figsize=(20,12))

ii = 1
for cm in cml:

    ax = fig.add_subplot(6,14,ii)

    ax.pcolormesh(XX,YY,z, cmap=cm)
    ax.axis('square')
    ax.set_axis_off()
    ax.set_title(cm)

    ii += 1
    
fig.tight_layout()

plt.show()