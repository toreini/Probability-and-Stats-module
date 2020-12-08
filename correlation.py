import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = list(range(-10, 11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]
x_, y_ = np.array(x), np.array(y)
x__, y__ = pd.Series(x_), pd.Series(y_)


n = len(x)
mean_x, mean_y = sum(x) / n, sum(y) / n
cov_xy = (sum((x[k] - mean_x) * (y[k] - mean_y) for k in range(n))/ (n - 1))

#NumPy has the function cov() that returns the covariance matrix:
cov_matrix = np.cov(x_, y_)

#Note that cov() has the optional parameters bias, 
# which defaults to False, and ddof, which defaults to None. 
# Their default values are suitable for getting the sample covariance matrix. 
# The upper-left element of the covariance matrix is the covariance of x and x, or the variance of x. 
# Similarly, the lower-right element is the covariance of y and y, or the variance of y. 

# Pandas Series have the method .cov() that you can use to calculate the covariance:
cov_xy = x__.cov(y__)


# The correlation coefficient, or Pearson product-moment correlation coefficient, is denoted by the symbol 𝑟.

var_x = sum((item - mean_x)**2 for item in x) / (n - 1)
var_y = sum((item - mean_y)**2 for item in y) / (n - 1)
std_x, std_y = var_x ** 0.5, var_y ** 0.5
r = cov_xy / (std_x * std_y)

# scipy.stats has the routine pearsonr() that calculates the correlation coefficient and the 𝑝-value
r, p = scipy.stats.pearsonr(x_, y_)

# you can apply np.corrcoef() with x_ and y_ as the arguments and get the correlation coefficient matrix
corr_matrix = np.corrcoef(x_, y_)

# You can get the correlation coefficient with scipy.stats.linregress():
result = scipy.stats.linregress(x_, y_)
r = result.rvalue

# Pandas Series have the method .corr() for calculating the correlation coefficient
r = x__.corr(y__)


