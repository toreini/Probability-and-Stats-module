import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
from scipy.stats import ttest_1samp
import numpy as np

# you have 10 ages and you are checking whether avg age is 30 or not. 

ages = np.genfromtxt("ages.txt")
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
tset, pval = ttest_1samp(ages, 30)
print("p-values",pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

# Z Test: Python does not focus much on Z Test comparing to T Test but you can call statsmodels.stats module for z Test (or implement your own p-value)

""" A common perception about COVID-19 is that Warm Climate is more resistant to the corona outbreak and we need to verify this using Hypothesis Testing. So what will our null and alternate hypothesis be?

Null Hypothesis: Temperature doesn’t affect COV-19 Outbreak
Alternate Hypothesis: Temperature does affect COV-19 Outbreak
Note: We are considering Temperature below 24 as Cold Climate and above 24 as Hot Climate in our dataset.
 """

corona = pd.read_csv('Corona_Updated.csv')
corona['Temp_Cat'] = corona['Temprature'].apply(lambda x : 0 if x < 24 else 1)
corona_t = corona[['Confirmed', 'Temp_Cat']]

def TwoSampZ(X1, X2, sigma1, sigma2, N1, N2):
    from numpy import sqrt, abs, round
    from scipy.stats import norm
    ovr_sigma = sqrt(sigma1**2/N1 + sigma2**2/N2)
    z = (X1 - X2)/ovr_sigma
    pval = 2*(1 - norm.cdf(abs(z)))
    return z, pval

d1 = corona_t[(corona_t['Temp_Cat']==1)]['Confirmed']
d2 = corona_t[(corona_t['Temp_Cat']==0)]['Confirmed']

m1, m2 = d1.mean(), d2.mean()
sd1, sd2 = d1.std(), d2.std()
n1, n2 = d1.shape[0], d2.shape[0]

z, p = TwoSampZ(m1, m2, sd1, sd2, n1, n2)

z_score = np.round(z,8)
p_val = np.round(p,6)

if (p_val<0.05):
    Hypothesis_Status = 'Reject Null Hypothesis : Significant'
else:
    Hypothesis_Status = 'Do not reject Null Hypothesis : Not Significant'

print (p_val)
print (Hypothesis_Status)


# collect the blood pressure for an individual before and after some treatment, condition, or time point.
#H0 :- means difference between two sample is 0
#H1:- mean difference between two sample is not 0

# check the code below for same


df = pd.read_csv("blood_pressure.csv")
df[['bp_before','bp_after']].describe()

ttest,pval = stats.ttest_rel(df['bp_before'], df['bp_after'])
print(pval)
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

ztest ,pval = stests.ztest(df['bp_before'], x2=None, value=156)
print(float(pval))
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")