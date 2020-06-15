"""
A masked array is like a numpy array except that it is meant to include
missing values (like land values in an ocean model).  To do this it stores
the data in TWO arrays, e.g.: a.data for the data and a.mask, a Boolean array
of the same shape that is True at masked locations in the array.
"""

# imports
import numpy as np
import matplotlib.pyplot as plt

# make an array
N = 10
# box edges
X = np.linspace(-1,1,N+1)
Y = np.linspace(-1,1,N+1)
XX, YY = np.meshgrid(X,Y)
# box centers and data
x = X[:-1] + np.diff(X)/2
y = Y[:-1] + np.diff(Y)/2
xx, yy = np.meshgrid(x,y)
r = np.sqrt((xx-.25)**2 + (yy-.5)**2)

# original data array
a = np.cos(8*r) + xx

# make a masked array
mask = a >= 0.5
am = np.ma.masked_where(mask, a)
    
# and a version of the data array with Nan's at masked locations
anan = a.copy()
anan[mask] = np.nan

# exploration of properties
def ismasked(a):
    #
    if isinstance(a, np.ma.MaskedArray):
        ismasked = True
    else:
        ismasked = False
    return ismasked

print(30*'-=')
a_dict = {'a':a, 'am':am, 'anan':anan}
for k in a_dict.keys():
    print('\n'+k+':')
    ism = ismasked(a_dict[k])
    if ism:
        print('- IS a masked array, Hooray!')
    else:
        print('- is NOT a masked array')
        
print(30*'-=')
# operations on masked arrays typically ignore the masked part
print('\nam.mean()')
print(am.mean())
#
print('\nanan.mean()')
print(anan.mean())
#
print('\nnp.nanmean(anan)')
print(np.nanmean(anan))
#
print('\nanan[~mask].mean()')
print(anan[~mask].mean())

print(30*'-=')
# you can get the separate parts using .data and .mask
print('\nam.data')
print(am.data)
#
print('\nam.mask')
print(am.mask)

# Plotting
vlim = 2
plt.close('all')
fig = plt.figure(figsize=(10,5))

ax = fig.add_subplot(121)
ax.pcolormesh(XX,YY,a, vmin=-vlim, vmax=vlim)
ax.set_title('original array')

ax = fig.add_subplot(122)
ax.pcolormesh(XX,YY,am, vmin=-vlim, vmax=vlim)
ax.set_title('masked array')

plt.show()
