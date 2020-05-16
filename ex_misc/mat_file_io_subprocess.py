"""
Here we write a numpy array or arrays to disk formatted as MATLAB
.mat files, and then use the subprocess module to run matlab code on the file
and save it. Then we read the new mat-file back into python.

NOTE: becauae subprocess spawns a complately independent job you can start
as many jobs as you like simlutaneously - or at least as many as you have cores
available. To do this you should omit the stdout and stderr arguments
passed to subprocess.run() because for some reason they make the calling
program wait until the previous subprocess is done.

NOTE: you can run other python programs this way, or really any program.  It
is not limited to MATLAB.

NOTE: to get this to run you will HAVE to edit the line:
cmd = '/Applications/MATLAB_R2017a.app/bin/matlab'
to reflect where MATLAB is on your machine.  On fjord it would be:
cmd = '/usr/local/bin/matlab'

"""

# imports
import numpy as np
from scipy import io
import subprocess

import sys, os
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
# make sure the output directory exists
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
mymod.make_dir(out_dir)

# define the output filenames
fn1 = 'mat_1.mat' # the one we will create
fn2 = 'mat_2.mat' # the one MATLAB will create and we will read

# delete these if they exist
for fn in [fn1, fn2]:
    if os.path.exists(out_dir + fn):
        os.remove(out_dir + fn)
    else:
        pass

# create arrays to save
a = np.linspace(0,3,10).reshape((5,2))
print('\nOriginal array a:')
print(a)

b = np.linspace(0,11,10).reshape((2,5))
print('\nOriginal array b:')
print(b)

# save the file to disk in .mat format
io.savemat(out_dir + fn1, {'a':a, 'b':b})
# One quirk is that we have to pass a dict {} of objects to save.
# This is useful because it allows us to pass multiple arrays
# to MATLAB and know what they will be called.

# use subprocess run a matlab function on it
#
func = "mat_worker(\'" + out_dir + "\',\'" + fn1 + "\',\'" + fn2 + "\')"
# a tedious way to form the string: mat_worker('../../pmec_output/','mat_1.mat','mat_2.mat')
#
cmd = '/Applications/MATLAB_R2017a.app/bin/matlab'
# for some reason I can't just use 'matlab'
#
run_cmd = [cmd, "-nodisplay", "-r", func, "&"]
# note: the run_cmd is a list []
# the -nodisplay is, I think just needed for MATLAB
# I forget what the -r is for, but it is needed
# and the & is the usual linux "escape to shell"
#
# run the worker job
proc = subprocess.run(run_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(50*'=')
print('*** screen output from worker:\n')
print(proc.stdout.decode())
print(50*'=')
print('*** error messages from worker:\n')
print(proc.stderr.decode())
print(50*'=')
# NOTE: you can omit the "stdout=subprocess.PIPE, stderr=subprocess.PIPE"
# parts of the .run command, but they can be helpful for looking at what happened
# or what went wrong

# now load the matfile created by MATLAB
x = io.loadmat(out_dir + fn2)
# what we find is that x is a dict with (among other things) the keys
# 'aa' and 'bb'

aa = x['aa']
bb = x['bb']

print('\nReturned aa:')
print(aa)

print('\nReturned bb:')
print(bb)

