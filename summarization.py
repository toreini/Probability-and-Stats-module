import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

#Measures of Central Tendency

x = [8.0, 1, 2.5, 4, 28.0]
y = np.array(x)
z= pd.Series(x)

mean_ = sum(x) / len(x)

#Next: We called the functions mean() and fmean() from the built-in Python statistics library and got the same result 
# as you did with pure Python. 
# fmean() is introduced in Python 3.8 as a faster alternative to mean(). 
mean_ = statistics.mean(x)
mean_ = statistics.fmean(x)

#If you use NumPy, then you can get the mean with np.mean()
mean_ = np.mean(y)

#In the example above, mean() is a function, but you can use the corresponding method
mean_ = y.mean()


# pd.Series objects also have the method.
# As you can see, it’s used similarly as in the case of NumPy. 
# However, .mean() from Pandas ignores nan values by default

mean_ = z.mean()


# The sample median is the middle element of a sorted dataset. 
# The dataset can be sorted in increasing or decreasing order. 
# If the number of elements 𝑛 of the dataset is odd, 
# then the median is the value at the middle position: 0.5(𝑛 + 1). 
# If 𝑛 is even, then the median is the arithmetic mean of the two values in the middle, 
# that is, the items at the positions 0.5𝑛 and 0.5𝑛 + 1.

n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])

# You can get the median with statistics.median():
median_ = statistics.median(x)

# You can also get the median with np.median():
median_ = np.median(y)

# Pandas Series objects have the method .median() that ignores nan values by default:
z.median()

## Mode

#The sample mode is the value in the dataset that occurs most frequently. 
# If there isn’t a single such value, then the set is multimodal since it has multiple modal values. 

u = [2, 3, 2, 8, 12]
mode_ = max((u.count(item), item) for item in set(u))[1]

# You can obtain the mode with statistics.mode() and statistics.multimode():
mode_ = statistics.mode(u)
mode_ = statistics.multimode(u)

# The sample variance quantifies the spread of the data. 
# It shows numerically how far the data points are from the mean. 

n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_)**2 for item in x) / (n - 1)

# the shorter and more elegant solution is to call the existing function statistics.variance()
var_ = statistics.variance(x)

# You can also calculate the sample variance with NumPy. 
# You should use the function np.var() or the corresponding method .var()
# It’s very important to specify the parameter ddof=1. 
# That’s how you set the delta degrees of freedom to 1. 
# This parameter allows the proper calculation of 𝑠², with (𝑛 − 1) in the denominator instead of 𝑛.

var_ = np.var(y, ddof=1)
var_ = y.var(ddof=1)

# pd.Series objects have the method .var() that skips nan values by default:
z.var(ddof=1)

# You calculate the population variance similarly to the sample variance. 
# However, you have to use 𝑛 in the denominator instead of 𝑛 − 1: Σᵢ(𝑥ᵢ − mean(𝑥))² / 𝑛. 
# In this case, 𝑛 is the number of items in the entire population. 
# You can get the population variance similar to the sample variance, with the following differences:

# (1) Replace (n - 1) with n in the pure Python implementation.
# (2) Use statistics.pvariance() instead of statistics.variance().
# (3) Specify the parameter ddof=0 if you use NumPy or Pandas. 
# In NumPy, you can omit ddof because its default value is 0.


## Standard Deviation
# The sample standard deviation is another measure of data spread.

std_ = var_ ** 0.5

# you can also use statistics.stdev():
std_ = statistics.stdev(x)

# You can get the standard deviation with NumPy in almost the same way. 
# You can use the function std() and the corresponding method .std() to calculate the standard deviation.
# Don’t forget to set the delta degrees of freedom to 1!

np.std(y, ddof=1)

# pd.Series objects also have the method .std() that skips nan by default:
z.std(ddof=1)

# The population standard deviation refers to the entire population. 
# It’s the positive square root of the population variance. 
# You can calculate it just like the sample standard deviation, with the following differences:

# (1) Find the square root of the population variance in the pure Python implementation.
# (2) Use statistics.pstdev() instead of statistics.stdev().
# (3) Specify the parameter ddof=0 if you use NumPy or Pandas. 
# In NumPy, you can omit ddof because its default value is 0.

## Summary of Descriptive Statistics

# SciPy and Pandas offer useful routines to quickly get descriptive statistics with a single function or method call. 
# You can use scipy.stats.describe() like this:

result = scipy.stats.describe(y, ddof=1, bias=False)

# The output will be: 
# DescribeResult(nobs=9, minmax=(-5.0, 41.0), mean=11.622222222222222, variance=228.75194444444446, skewness=0.9249043136685094, kurtosis=0.14770623629658886)

# describe() returns an object that holds the following descriptive statistics:

# nobs: the number of observations or elements in your dataset
# minmax: the tuple with the minimum and maximum values of your dataset
# mean: the mean of your dataset
# variance: the variance of your dataset
# skewness: the skewness of your dataset (The sample skewness measures the asymmetry of a data sample.)
# kurtosis: the kurtosis of your dataset (The sample kurtosis measures of the "tailedness" of a data sample.)


# Pandas has similar, if not better, functionality. Series objects have the method .describe():

result = z.describe()

# The output will be: 
# count     9.000000
# mean     11.622222
# std      15.124548
# min      -5.000000
# 25%       0.100000
# 50%       8.000000
# 75%      21.000000
# max      41.000000
# dtype: float64

# count: the number of elements in your dataset
# mean: the mean of your dataset
# std: the standard deviation of your dataset
# min and max: the minimum and maximum values of your dataset
# 25%, 50%, and 75%: the quartiles of your dataset

















