# Intro to Xarray
# Derya Gumustel

# Need to have xarray module, which is not part of the standard
# anaconda installation.  I got it by doing "pip install xarray"
# at the linux prompt. (P. MacCready 2020.05.26)

import numpy as np
import pandas as pd
import xarray as xr


# Creating a random DataArray 
data = xr.DataArray(np.random.randn(4, 6), dims=('x', 'y'), coords={'x': [10, 20, 30, 40]})

# Another way to create a DataArray:
#data = xr.DataArray(pd.Series(range(3), index=list('abc'), name='foo'))

# Attributes are metadata, like variable descriptions and units. Contained in a dictionary.
print('\n')
print('Add metadata to a variable \n')
data.attrs['long_name'] = 'random velocity'
data.attrs['units'] = 'metres/sec'
data.attrs['description'] = 'A random variable created as an example.'
data.attrs['random_attribute'] = 123
print(data.attrs)

# Coordinates can have their own attributes.
print('\n \n')
print('Add metadata to a coordinate \n')
data.x.attrs['units'] = 'x units'
data.x.attrs['description'] = 'A random coordinate created as an example.'
print(data.x)

# Check values in array
print('\n \n')
print('Look at data values \n')
print(data.values)

# Do some simple manipulation:
print('\n')
print('Do math \n')
print(data + 10)
#print(np.sin(data))
#print(data.T)
#print(data.sum())

# You can also perform statistics along specified dimensions
print('\n') 
print('Do stats \n')
print(data.mean(dim='x'))
print(data.std(dim='x'))

# Xarray data structures can be turned into pandas data structures and vice versa
series = data.to_series()
print('\n')
print(series)
data = series.to_xarray()
print('\n')
print(data)


# INDEXING
#data[0,:]
#data.loc[10]
#data.isel(x=0)
#data.sel(x=10)


# Opening an existing netCDF file as a dataset:
#argo1_ds = xr.open_dataset(data_dir + '/filename.nc')
#argo1_df = argo1_ds['TEMP'].to_dataframe()    # turn one variable from the dataset into a pandas DataFrame

