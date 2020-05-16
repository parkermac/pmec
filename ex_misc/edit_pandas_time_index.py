"""
Edit a time in a pandas DataFrame index.

"""

# this is the standard way to import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# make some heterogenous data
#
# start by making the "index" that will be used to align all the
# other data.  In this case we generate a sequence of times.
t = pd.date_range(start='5/1/2020' , end='5/5/2020', freq='12H')
# make other data vectors
N = len(t)
x1 = np.arange(N) + np.random.randn(N)
x2 = x1**2
c = []
for item in x1:
    if item < 5:
        c.append('red')
    else:
        c.append('green')

# then create the DataFrame and put the data in it
df = pd.DataFrame(index=t)
df['x1'] = x1
df['x2'] = x2
df['color'] = c
df.index.name = 'date'

# Edit a single time in the index by hand:

# get the index (a pandas object)
aa = df.index
# use dir(aa) to find methods for pandas Index objects
# for example you could set the time zone:
# aa_utc = aa.tz_localize('UTC')
# and then convert it to Pacific time:
# aa_pac = aa_utc.tz_convert('US/Pacific')

# get the index as an array of datetimes, because you can't edit a
# pandas index directly
a = aa.to_pydatetime()

# add 5 hours to the first time
a[0] = a[0] + timedelta(hours=5)

# then create a new DataFrame, using the original data
# and the new index
df_new = df.set_index(a)





