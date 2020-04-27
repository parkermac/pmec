"""
Code to demonstrate using pickle to save an array to disk,
and get it back again.
"""

#imports
import sys, os
import numpy as np
import pickle

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

# make an array
a = np.linspace(0,10,10000).reshape((2,5,1000))

# save it as a pickle file
out_fn = out_dir + 'pickled_array.p'
pickle.dump(a, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
b = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

print('\nThe shape of the loaded object is')
print(b.shape)

# we could use pickle to save any python object, including a list
# or a dict of other objects

# Question: how much space does a pickle file with 10000 floating point
# numbers take up on your disk?  What does this tell you about how big
# each number is (how many bytes? how many bits?)

