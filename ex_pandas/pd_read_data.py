"""
Code to explore reading data from csv and xlsx files.  Thanks to
Theresa Whorley for providing the files.

NOTE: This is real data that has not been published and to please use it respectfully,
i.e. not outside of the context of this class.

"""

# imports
import pandas as pd
import matplotlib.pyplot as plt

# names of files to open
csv_fn = '../../pmec_data/Whorley_C2016major_Grn.csv'
xlsx_fn = '../../pmec_data/Whorley_TN_314_Analyses.xlsx'

# load files int DataFrames
df1 = pd.read_csv(csv_fn)
df2 = pd.read_excel(xlsx_fn, sheet_name='Water Column', skiprows=3)

# extract just the rows of df2 that correspond to a chosen CTD cast
df2a = df2[df2['Sample #'].str.contains('CTD 1-', na=False)].copy()
"""
Deconstructing the line of code above:

df2['Sample #'] is a pandas "Series" essentially just one column of df2

.str is a method of the Series that allows you to do operations on the
contents of the Series all at once ("vectorized")

What we do is look for the entries in df2['Sample #'].str that contain
the substring 'CTD 1-'.  We do this using the .contains() method.

We have to pass the keyword argument na=False because there are missing
values in the Series that can't be parsed as strings.

Finally we use the .copy() method to make sure the the df2a DataFrame we create
is a new object, not just a view into the df2.  We need to do this or else
the step below of adding a column throws a warning.
"""

# make a new column that has a z-coordinate of the right sign
df2a['Z (m)'] = - df2a['Depth (mbsl)']

# PLOTTING
plt.close('all')

df2a.plot(x='Salinity', y='Z (m)')

plt.show()

"""
CHALLENGE: for df1 Theresa writes:

"For the CSV file, I would typically want to find the mean, standard deviation,
and percent relative standard deviation for the five replicates of each analyte
within each sample and then transpose the entire matrix so that each sample was
a row and each analyte was a column."

Can you write code that will do this for her?
"""

