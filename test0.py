"""
This code is to test calling a function.
"""
import numpy as np # do imports first

def my_fun(x): # function to compute the sine of the square
    y = np.sin(x**2)
    return y

for xx in np.linspace(0, 2*np.pi, 12):
    yy = my_fun(xx)
    print('x = %0.2f, y = %0.2f' % (xx, yy))

# that's it!
