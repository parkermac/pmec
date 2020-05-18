"""
Attempt to read and manipulate data using pandas, then plot some of it.
I've attempted to read in the ICP-OES file 'Whorley_C2016major_Grn.csv' and I'll try
to find the average and standard deviation of each analyte, 5 replicates per analyte.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Local Imports, File Paths
import os, sys
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
myplace = 'pmec'

# Input / Output Directories
in_dir = '../../' + myplace + '_data/'
out_dir = '../../' + myplace + '_output/'

#Define Input / Output File Names
in_fn = in_dir + 'Whorley_C2016major_Grn.csv'
out_fn = out_dir + 'C2016maj.png'

# Read in the data file
df = pd.read_csv(in_fn)

df.drop(['Date', 'Time', 'Elem', 'Int (Corr)', 'RSD (Corr Int)', 'SD (Corr Int)',
        'Date1', 'Time1', 'Date2', 'Time2', 'Date3', 'Time3', 'Date4', 'Time4', 
        'Date5', 'Time5'], axis=1, inplace=True)   # delete useless columns

df.drop(['Int (Corr)1', 'Int (Corr)2', 'Int (Corr)3', 'Int (Corr)4', 'Int (Corr)5'],
        axis=1, inplace=True)   # delete more useless columns; don't care about corrected intensities

# Re-Index so that 'Sample ID' is the new index, not sample run number (1-2720)
df.set_index('Sample ID', inplace=True)   #if i ask the data 'df.index.is_unique' it should return "False"


# Make 3 new empty columns for Average Int (Net), Std Int (Net), and %RSD Int (Net)
df['Avg Net Int'] = ""
df['Std Net Int'] = ""
df['%RSD Net Int'] = ""
print(df.dtypes)   # these new columns are added as object dtypes


# Find average of 5 replicate net intensities, put in 'Avg Net Int' column
"""
This is super difficult because my 'Int (Net)#' columns are python objects, not float64 type.
Can find out the dtype of each columns by running the command 'df.dtypes'
—- Tried to use " df['Int (Net)1'] = pd.to_numeric(df['Int (Net)1']) " but there was an error
    Unable to parse string " " at position 147
-- Tried to use " df['Int (Net)1'] = df.astype(float) " but returned the error
    could not convert string to float
-- Tried " for i in range(0, len(df.columns)):
                df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], errors='ignore')
    This changed my newly added three columns (Lines 44-46 in code) to float64 dtypes, but nothing else
"""

# for i in range(0, len(df.columns)):
#     df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], errors='ignore')  # only works for last 3 columns

for vn in ['Int (Net)1','Int (Net)2','Int (Net)3','Int (Net)4','Int (Net)5',]:
    df[df[vn] == ' '] = np.nan
    df[vn] = pd.to_numeric(df[vn])
    print(df[vn].mean())
    
print(df.dtypes)


# I'm going to abandon ship so I can complete the assignment and see if working with a smaller
#portion of the data helps.
# grab just the first 80 reads, all are initial 'Blank' solution readings
blank = df[:80]   
# Same issues. Can't find a way to convert the 'Int (Net)#' columns into float64 dtypes.





# Final Step: transpose the DataFrame using: df.T