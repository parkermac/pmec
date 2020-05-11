"""
Code to introduce pandas DataFrames and Series.

"""

# this is the standard way to import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# make some heterogenous data
t = pd.date_range(start='5/1/2020' , end='5/5/2020', freq='12H')
N = len(t)
x1 = np.arange(N) + np.random.randn(N)
x2 = x1**2
c = []
for item in x1:
    if item < 5:
        c.append('red')
    else:
        c.append('green')
        
df = pd.DataFrame(index=t)
df['x1'] = x1
df['x2'] = x2
df['color'] = c
df.index.name = 'date'

def sep():
    print('\n'+60*'-'+'\n')

sep()
print('The original DataFrame')
print(df)

sep()
print('Select a single column - this returns a pandas Series')
print("df['x1']:\n")
print(df['x1'])

sep()
print('Select all rows using a condition from one column')
print("df[df['color']=='green']:\n")
print(df[df['color']=='green'])

sep()
print('Select a range of rows and columns')
print('(Note that the date range is inclusive of the end point)')
print("df.loc[datetime(2020,5,1):datetime(2020,5,3,12),['x1','color']]:\n")
print(df.loc[datetime(2020,5,1):datetime(2020,5,3,12),['x1','color']])

# other things to explore

# make a new column out of the index (changes df)
# df['date'] = df.index
# this would be useful if you wanted to temporarily make a different
# variable be the index, but still keep 'date' around

# make one of the columns be the index
# df.set_index('x2')

# drop a column
# df.drop(labels='x2',axis=1)

# make 2-day averages
# df.resample('2D').mean()

if True:
    # PLOTTING
    plt.close('all')

    tstr = 'Basic plot of two columns'
    df[['x1','x2']].plot(title=tstr)

    tstr = 'Plot with more control'
    df[['x1','x2']].plot(title=tstr, style=['-o','--*'],
        markersize=15, linewidth=3, grid=True)

    plt.show()

