"""
Notes on the Whorley challenge
"""
# Imports
import numpy as np
import pandas as pd

# Local Imports, File Paths
myplace = 'pmec'

# Input / Output Directories
in_dir = '../../' + myplace + '_data/'

#Define Input / Output File Names
in_fn = in_dir + 'Whorley_C2016major_Grn.csv'

# Read in the data file
df = pd.read_csv(in_fn)

# Fixes to the missing values that have a space
# Parker
for vn in ['Int (Net)1','Int (Net)2','Int (Net)3','Int (Net)4','Int (Net)5',]:
    df[df[vn] == ' '] = np.nan
    df[vn] = pd.to_numeric(df[vn])
    print(df[vn].mean())
    
"""
# Rita
df_reduced = df_reduced.apply(pd.to_numeric, args=('coerce',))

# Erik
# replace missing Int (Corr) values with NaNs, convert to floats
df_tw3 = df_tw2.replace(to_replace=' ',value='NaN')
df_tw4 = df_tw3.astype('float64')

# Alex
for replicate in replicateNames:
    data_df[replicate] = pd.to_numeric(data_df[replicate], errors='coerce')
    
# Jiwoon
df = pd.read_csv("Whorley_C2016major_Grn.csv", na_values = [' '])

# Jade
df1 = pd.read_csv(directory_in+file_in1,na_values=' ',dtype=col_dict)
df1_mean = df1[col_list].mean(axis=1,skipna=True)
    
"""