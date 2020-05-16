"""
This code puts some data, and associated metadata like axes and units,
into a NetCDF file. Then it reads back a part of that data. Also shows editing.

NetCDF is the standard format for many gridded scientific datasets.
It is awesome because it associates physical axes with array dimensions


"""

# imports
import numpy as np
import netCDF4 as nc # this is the important module
from datetime import datetime, timedelta

import sys, os
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
# make sure the output directory exists
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
mymod.make_dir(out_dir)

# define the output filename
out_fn = 'netcdf_1.nc'
# delete it if it exists (essential for creating NetCDF files)
if os.path.exists(out_dir + out_fn):
    os.remove(out_dir + out_fn)
else:
    pass

# create data to save
#
# coordinates
lon = np.linspace(-130,-120,100)
lat = np.linspace(40,50,200)
tvec = []
t0 = datetime(2020,1,1)
for dt in range(10):
    tvec.append(t0 + timedelta(days=dt))
# convert from datetimes to seconds since 1/1/1970
ttvec = []
tt0 = datetime(1970,1,1)
for t in tvec:
    ttvec.append(86400*((t - tt0).days))
# get sizes
NX = len(lon)
NY = len(lat)
NT = len(ttvec)
# make data
Lon, Lat = np.meshgrid(lon,lat)
V = np.cos(Lon) + Lat**2
VV = np.nan * ( np.ones((NT, NY, NX)))
for ii in range(NT):
    VV[ii, :, :] = ii * V

# intialise the NetCDF object
# (foo is a common coder name for a temporary thing)
foo = nc.Dataset(out_dir + out_fn, 'w')

# create dimensions
foo.createDimension('x', NX)
foo.createDimension('y', NY)
foo.createDimension('t', NT)
# use "foo.createDimension('t', None)" if we don't know how long it will be
# this is called an 'unlimited dimension'

# create variable objects
# I just recycle v_var each time
v_var = foo.createVariable('lon', float, ('x'))
v_var.long_name = 'Longitude'
v_var.units = 'degrees'
#
v_var = foo.createVariable('lat', float, ('y'))
v_var.long_name = 'Latitude'
v_var.units = 'degrees'
#
v_var = foo.createVariable('ts', float, ('t'))
v_var.long_name = 'Time in seconds since 1/1/1970'
v_var.units = 'seconds'
#
v_var = foo.createVariable('fld', float, ('t', 'y', 'x'))
v_var.long_name = 'Data Field'
v_var.units = 'parsnips per petabyte'
#
# put data in the variables
foo['lon'][:] = lon
foo['lat'][:] = lat
foo['ts'][:] = ttvec
foo['fld'][:] = VV
#
# all done creating it
foo.close()

# now let's read it
ds = nc.Dataset(out_dir + out_fn)
# pull out a little piece
a = ds['fld'][:,10,10]
print('\nORIGINAL\n'+ds['fld'].name)
print(ds['fld'].long_name)
print(ds['fld'].units)
print(a)
ds.close()

# edit a value by hand
ds = nc.Dataset(out_dir + out_fn, 'a')
ds['fld'][0,10,10] = 47
ds.close()

# and read it again
ds = nc.Dataset(out_dir + out_fn)
# pull out a little piece
a = ds['fld'][:,10,10]
print('\nEDITED\n'+ds['fld'].name)
print(ds['fld'].long_name)
print(ds['fld'].units)
print(a)
#ds.close()

# NOTE: try ds.variables (before closing it) and look at the output



