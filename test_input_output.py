"""
Code to test input and (filtered) output of a text file.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod

myplace = 'pmec' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filename
out_fn = out_dir + 'out_test.txt'

# open the output file for writing
outfile = open(out_fn, 'w')

# create a dict for translating direction letters to numbers
sign_dict = {'N':1,'S':-1,'E':1,'W':-1}

# go through the input file one line at a time, and just
# write decimal versions of the latitude and longitude
# to the output file
with open(in_fn, 'r', errors='ignore') as f:
    # typical real-world issue: the read operation throws an error
    # around line 383 for unknown reasons - we ignore it.
    for line in f:
        
        if 'LATITUDE' in line:
            LS = line.split() # .split() makes a list out of the separate items in line
            degs = LS[2]
            mins = LS[3]
            sign = LS[4]
            # have to turn text things into numbers using float([string])
            lat = sign_dict[sign] * (float(degs) + float(mins)/60)
            # write a line to the outfile
            outfile.write('y = %0.3f\n' % (lat))
            # and write to the screen
            print('y = %0.3f' % (lat))
            
        if 'LONGITUDE' in line:
            LS = line.split()
            degs = LS[2]
            mins = LS[3]
            sign = LS[4]
            lon = sign_dict[sign] * (float(degs) + float(mins)/60)
            outfile.write('x = %0.3f\n' % (lon))
            print('x = %0.3f' % (lon))

# close the output file
outfile.close()