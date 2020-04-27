# -*- coding: utf-8 -*-
"""
Code to test the calculation of the correlation coefficient "r"
for a pair of vectors.

The first method is doing it from scratch as in Emery and Thomson (1998)
eqn. (3.13.1a) and we compare this with alternates from numpy.

RESULT: All three give identical results.  Note that you have to select
one element of the 2x2 matrices: R1[0,1] and R2[0,1] in order to 
compare these with "r".  Note the use of ddof=1 in some places, which
amounts to dividing by N-1 when calculating a mean (the "unbiased" estimator).

RESULT : Use r = np.corrcoef(y1, y2)[0,1] as the simplest solution.

"""

import numpy as np
import matplotlib.pyplot as plt

# make a couple of vectors to correlate
N = 100 # number of points
x = np.linspace(0, 100, N)
a = 1; b = 0.5; c = 0.5
def make_y(a, b, c, N):
    y = a * np.cos(x/5) + b * np.cos(x/8) + c * np.random.randn(N)
    return y
y1 = make_y(a, b, c, N)
y2 = make_y(a, b, c, N) + 3

# Calculate the correlation coefficient three ways

# 1 from scratch
r_from_scratch = ((y1-y1.mean()) * (y2-y2.mean())).sum() / ((N-1) * y1.std(ddof=1) * y2.std(ddof=1))

# 2 from numpy functions cov() and std()
R_cov = (np.cov(y1,y2) / (y1.std(ddof=1) * y2.std(ddof=1)))
r_cov = R_cov[0,1]

# 3 from numpy directly
R_corrcoef = np.corrcoef(y1,y2)
r_corrcoef = R_corrcoef[0,1]

#%% plotting
plt.close('all')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y1, y2, '.r')
ax.text(.05,.9,'r: from scratch = %0.4f' % (r_from_scratch), transform=ax.transAxes)
ax.text(.05,.8,'r: numpy cov and std = %0.4f' % (r_cov), transform=ax.transAxes)
ax.text(.05,.7,'r: np.corrcoef = %0.4f' % (r_corrcoef), transform=ax.transAxes)
plt.show()

