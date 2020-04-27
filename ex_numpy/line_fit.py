"""
Code to test fitting a line to some points, including the 95% confidence
interval on both the mean and the slope
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# make some data to fit
N = 50
x = np.linspace(0,1,N)
y_0 = 5 # y-intercept
dydx = 1 # slope
y_std = .1
y_noise = y_std * np.random.randn(N)
# original points
y = dydx*x + y_0 + y_noise

# Fit the line, following Emery and Thomson (1998) 3.12.4
#
# first make the input arrays
Y = y.reshape(N,1)
X = np.concatenate( (np.ones((N,1)), x.reshape(N,1)), axis=1)
# then do the fit
B = np.linalg.inv(X.T @ X) @ (X.T @ Y) # @ is matrix multiplication
# and unpask the result
yy_0 = B[0,0] # y-intercept
dyydx = B[1,0] # slope
# fit line
yy = dyydx*x + yy_0

# Calculate the 95% confidence interval for the mean and trend
# NOTE the call to the inverse cumulative Student's t-distribution:
# stats.t.ppf(1-.025,100) which is identical to MATLAB tinv(1-.025,100).
ci_pct = 95 # Confidence interval %
ci_fac = (1 - ci_pct/100)/2 # = 0.025 for ci_pct = 95
s_eps = np.sqrt(((y-yy)**2).sum()/(N-2)) # standard error of the estimate
s_x = x.std(ddof=1)
s_y = y.std(ddof=1)
# Condidence interval on mean: Emery and Thomson (3.8.6)
ci_mean = s_y * stats.t.ppf(1-ci_fac,N-1) / np.sqrt(N)
# Confidence interval on slope: Emery and Thomson (3.15.12b) w/typo corrected
ci_trend = s_eps * stats.t.ppf(1-ci_fac,N-2) / np.sqrt((N-1)*s_x*s_x)

# Alternatively, fit the line using python tools
BB = np.polyfit(x,y,1, full=True)
dyydx_alt = BB[0] # slope
yy0_alt = BB[1] # y-intercept
# RESULT: these are identical to the y-intercept and slope
# that I calculate from scratch above.

# plotting
fs = 14
plt.close('all')
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.plot(x, y, '*b', label='Data')
ax.plot(x, yy, '-r', label='Fit Line')
lh = ax.legend(loc='lower right')
plt.setp(ax.get_legend().get_texts(), fontsize=fs) 
ax.text(.05, .9, '$Mean = %0.5f \pm %0.4f$' % (y.mean(), ci_mean),
    transform=ax.transAxes, size=fs)
ax.text(.05, .85, '$Slope = %0.5f \pm %0.4f$' % (dyydx, ci_trend),
    transform=ax.transAxes, size=fs)
ax.text(.05, .8, '95% Confidence Intervals',
    transform=ax.transAxes, size=fs)
ax.set_title('N = %d' % (N), size=fs+2)
plt.show()
