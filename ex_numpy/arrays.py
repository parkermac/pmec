"""
Code to explore operations on numpy arrays.
"""

# imports
import numpy as np

print('\nCreate a vector (a 1-D array) from a [list]')
a = np.array([1,2,3,4,5,6])
print(a)

print('\nIndexing is just like you learned for lists')
print('e.g. a[::2] gets every other item')
print(a[::2])

print('\nThe index of the last element is -1')
print('so a[-1] gives:')
print(a[-1])

# create 2-D arrays using arange and reshape
# - arange makes an array of integers, starting at 0
# - reshape reshapes an array according to the "size"
# in the tuple you pass to it.
aa = np.array(np.arange(12)).reshape((6,2))
bb = np.array(np.arange(12)).reshape((2,6))
print('\n2-D arrays of different shapes:')
print('\naa =')
print(aa)
print('\nbb =')
print(bb)

# indexing: for 2-D arrays:
# - axis 0 is the rows and
# - axis 1 is the columns,
# and you address each axis in turn in the [], separated by commas
print('\nIndexing a 2-D array: aa[:3, :]')
print(aa[:3, :]) # the second : means "all items of that axis"

print('\nElement-by-element operation (like .* in MATLAB): ')
#
print('\n - exponentiation')
print(aa**2.7) # exponentiation is **
#
print('\n - square root')
print(np.sqrt(aa)) # square root
#
print('\n - Error from aa + bb')
try:
    print(aa + bb) # addition (throws an error because aa and bb are different shapes)
except ValueError as err:
    print(err)
print('\n - aa + bb.T works')
print(aa + bb.T) # need to take transpose of bb so it has the same shape as aa

print('\nMatrix multiplication using @: aa @ bb')
print(aa @ bb)

print('\nMatrix multiplication using @: bb @ aa')
print(bb @ aa)

print('\nConcatenate two arrays')
cc = np.concatenate((aa,aa), axis=1)
print(cc)

print('\nFlatten and array')
print(aa.flatten())

print('\n Make a Boolean mask of aa >= 5')
mask = aa >= 5
print(mask)

print('\n Use the mask to get just those elements of aa: aa[mask]')
print(aa[mask])
print('Note that this returns just a 1-D arrray (flattened)')

"""
Exercises to try on your own:

What happens if you make a copy of a byt typing b = a,
and then change an element in a by hand?  Does b change as well?
Now try it again using the copy method b = a.copy() and see 
what happens.

To change an element by hand just assign it: a[3] = 17

You can convert an array of integers to an array of floats this way:
af = a.astype(float)

Figure out how to find the mean, standard deviation, max, and index of
the max of an array.

Missing data is represented as the number np.nan.  What happens if
you put a nan in your array and then calculate the mean?  You have
to convert the array to floats first before you can put a nan in.
Then also try the method np.nanmean() on the array with a nan.

Look around in other sub-modules using dir() and help():
* np.random (quickly generate arrays random numbers, e.g. np.random.randn())
* np.linalg (linear algebra stuff like the inverse of a matrix: np.linalg.inv())
* np.ma (masked arrays)
* scipy.stats (have to import scipy first)

"""


