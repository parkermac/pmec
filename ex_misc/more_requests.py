"""
Examples of getting data from web resouces using requests.

"""

# imports
import sys, os
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

import requests
import bs4
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# make sure the output directory exists
junk, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir)

plt.close('all')

do_ndbc = True
do_tide = True

if do_ndbc:
    # EXAMPLE 1: NDBC buoy data - historical for one year

    # Resources
    # https://www.ndbc.noaa.gov/
    # https://www.ndbc.noaa.gov/download_data.php?filename=46029h2018.txt.gz&dir=data/historical/stdmet/

    # station and year
    ndbc_sn = 46029 # Washington Shelf
    ndbc_year = 2018

    # get the data as a text file 
    try:
        # form the url string for the request
        idn = str(ndbc_sn) + 'h' + str(ndbc_year)
        ndbc_url = ('http://www.ndbc.noaa.gov/view_text_file.php?filename=' +
                   idn + '.txt.gz&dir=data/historical/stdmet/')
               
        # get the request and do some parsing
        html = requests.get(ndbc_url)
        soup = bs4.BeautifulSoup(html.content, 'html.parser')
        sn_text = soup.findAll(text=True)
    
        # some munging required
        sns = str(sn_text)[2:-2] # get rid of [' at start and '] at end
        sns = sns.replace('\\n','\n') # replace odd line feeds with real ones
    
        # write data to a text file
        ndbc_fn = out_dir + 'ndbc_' + idn + '.txt'
        f = open(ndbc_fn,'w')
        f.write(sns)
        f.close()
    
        print(' Retrieved ' + idn)
    except:
        print(' -- Failed ' + idn)
        pass

    # parse the text file into a pandas DataFrame
    ndbc_df = pd.read_csv(ndbc_fn, delim_whitespace=True, index_col='date',
             skiprows=[1],
             parse_dates={'date':[0, 1, 2, 3, 4]}, # the columns containing time info
             date_parser=lambda x: datetime.strptime(x, '%Y %m %d %H %M'))

    # plot one column
    ndbc_df[['WSPD']].plot()

if do_tide:
    # EXAMPLE 2: Tide station data for a year
    
    # Resources: NOAA Tides & Currents has awesome info
    # https://tidesandcurrents.noaa.gov/stationhome.html?id=9447130

    # station and year
    tide_sn = 9447130 # Seattle
    tide_year = 2018

    # form the URL string: note we are getting XML
    tide_url = ('https://tidesandcurrents.noaa.gov/api/datagetter?'
        + 'begin_date=' + str(tide_year) + '0101 00:00'
        + '&end_date=' + str(tide_year) + '1231 23:00'
        + '&station=' + str(tide_sn)
        + '&product=hourly_height'
        + '&datum=mllw&units=metric&time_zone=gmt'
        + '&application=University of Washington'
        + '&format=xml')
    
    # get the data from the web
    resp = requests.get(tide_url)
    
    # parsing the XML
    #
    # note that this is relatively simple - looking at the XML in Chrome:
    # <data>
    #     <metadata id="9447130" name="Seattle" lat="47.6026" lon="-122.3393"/>
    #     <observations>
    #         <hr t="2018-01-01 00:00" v="3.179" s="0.010" f="0,0"/>
    #         <hr t="2018-01-01 01:00" v="2.491" s="0.011" f="0,0"/>
    #         <hr t="2018-01-01 02:00" v="1.541" s="0.012" f="0,0"/>
    #         <hr t="2018-01-01 03:00" v="0.514" s="0.025" f="0,0"/> and so on
    #
    root = ET.fromstring(resp.text)
    # metadata
    m_dict = dict()
    m = root.find('metadata')
    for key in m.keys():
        m_dict[key] = m.attrib[key]
    # data
    t_list = []
    eta_list = []
    for e0 in root.findall('observations'):
        for e in e0.findall('hr'):
            t_list.append(e.attrib['t'])
            eta_list.append(float(e.attrib['v']))
    dti = pd.to_datetime(t_list)
    #dti = dti.tz_localize('UTC') # throws a warning: I'm not sure why
    tide_df = pd.DataFrame(data={'eta':eta_list}, index = dti)
    tide_df.index.name = 'Date'
    
    tide_df.plot()
    
plt.show()

