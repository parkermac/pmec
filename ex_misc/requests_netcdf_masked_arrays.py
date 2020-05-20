"""
Code to test getting a single time slice of HYCOM and plot it.
HYCOM is a global ocean model run by the US Navy.  It is data-assimilative
and makes daily forecasts about 10 days into the future.

General info:
https://www.hycom.org/

The specific product we are using:
https://www.hycom.org/dataserver/gofs-3pt1/analysis

Various ways to access the data
https://tds.hycom.org/thredds/catalogs/GLBy0.08/latest.html?dataset=GLBy0.08-latest

And a page about the access method we use here, including help on
formatting the URL for the request:
https://ncss.hycom.org/thredds/ncss/grid/GLBy0.08/latest/dataset.html

This is also a good opportunity to explore the properties of numpy "masked arrays"
which are often the result of reading fields from a NetCDF object.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

import netCDF4 as nc
import requests
from datetime import datetime, timedelta
import numpy as np
from time import time
import matplotlib.pyplot as plt

# make sure the output directory exists
junk, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir)

# specify the time for the requested field
dt = datetime.now()
dstr = dt.strftime('%Y-%m-%d-T00:00:00Z')

# name the output file
out_fn = out_dir + 'hycom_test.nc'
# because it is a NetCDF file we have to get rid of the existing
# version before getting the new one
try:
    os.remove(out_fn)
except OSError:
    pass # assume error was because the file did not exist

# form the 
if True:
    # just get SSH
    # url = ('https://ncss.hycom.org/thredds/ncss/GLBy0.08/'
    #     +'expt_93.0/FMRC/GLBy0.08_930_FMRC_best.ncd'
    #     + '?var=surf_el'
    #     + '&north=53&south=39&west=229&east=239'
    #     + '&time'+dstr
    #     + '&addLatLon=true&accept=netcdf4')
    url = ('https://ncss.hycom.org/thredds/ncss/GLBy0.08/'
        +'expt_93.0/FMRC/GLBy0.08_930_FMRC_best.ncd'
        + '?var=surf_el,salinity,water_temp'
        + '&north=53&south=39&west=229&east=239'
        + '&time'+dstr
        #+ '&vertCoord=1'
        + '&addLatLon=true&accept=netcdf4')
else:
    # get all variables
    url = ('https://ncss.hycom.org/thredds/ncss/GLBy0.08/'
        + 'expt_93.0/FMRC/GLBy0.08_930_FMRC_best.ncd'
        + '?var=surf_el,water_temp,salinity,water_u,water_v'
        + '&north=53&south=39&west=229&east=239'
        + '&time=' + dstr
        + '&addLatLon=true&accept=netcdf4')

def get_time(fn):
    # This function is just to make sure we got the expected time.
    # It is also an axample of using the datetime methods:
    # "strptime" to PARSE a formatted string into a datetime object, and
    # "strftime" to get a formatted string FROM a datetime object
    ds = nc.Dataset(fn)
    # get time info for the forecast
    t = ds['time'][0]
    # Caution: often when we get variables out of a NetCDF object
    # they are numpy "masked arrays" which are different than standard arrys
    if isinstance(t, np.ma.MaskedArray):
        th = t.data
    else:
        th = t
    tu = ds['time'].units
    # e.g. tu is 'hours since 2018-11-20 12:00:00.000 UTC'
    # Warning: Brittle code below!
    ymd = tu.split()[2]
    hmss = tu.split()[3]
    hms = hmss.split('.')[0]
    hycom_dt0 = datetime.strptime(ymd + ' ' + hms, '%Y-%m-%d %H:%M:%S')
    this_dt = hycom_dt0 + timedelta(days=(th/24))
    print('Target time = ' + dstr)
    print('Actual time = ' + this_dt.strftime('%Y-%m-%d-T00:00:00Z'))
    ds.close()

# get the data using requests.get()
tt0 = time()
if False:
    # streaming, chunked version
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(out_fn2, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
else:
    # regular version
    r = requests.get(url)
    with open(out_fn,'wb') as f:
        f.write(r.content)
        
print('\nrequests.get took %0.1f seconds' % (time()-tt0))
get_time(out_fn) # just checking

# pull out some fields
ds = nc.Dataset(out_fn)
x = ds['lon'][:]
if x.max() > 180:
    x = x - 360 # convert to -180:180 format
y = ds['lat'][:]
eta = ds['surf_el'][0,:,:]
salt = ds['salinity'][0,0,:,:]
temp = ds['water_temp'][0,0,:,:]

# PLOTTING
plt.close('all')
fig = plt.figure(figsize=(20,8))

ax = fig.add_subplot(131)
cs = ax.pcolormesh(x, y, eta - np.nanmean(eta), cmap='seismic')
mymod.dar(ax)
fig.colorbar(cs)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('HYCOM Surface Height [m] ' + dt.strftime('%Y-%m-%d'))

ax = fig.add_subplot(132)
cs = ax.pcolormesh(x, y, salt, cmap='Spectral_r',vmin=25)
mymod.dar(ax)
fig.colorbar(cs)
ax.set_xlabel('Longitude')
ax.set_title('Surface Salinity')

ax = fig.add_subplot(133)
cs = ax.pcolormesh(x, y, temp, cmap='viridis')
mymod.dar(ax)
fig.colorbar(cs)
ax.set_xlabel('Longitude')
ax.set_title('Surface Temperature')

plt.show()
