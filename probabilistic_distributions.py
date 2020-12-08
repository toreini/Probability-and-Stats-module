#%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


# -stats.distribution.rvs() generates random numbers from the specified distribution. 
data_uniform = stats.uniform.rvs(size=100000,  # Generate 100000 numbers
                                 loc = 0,      # From 0 
                                 scale=10)     # To 10
                                
# generate random numbers from N(0,1)
data_normal = stats.norm.rvs(size=10000,loc=0,scale=1)

# generate random numbers from Exponential Distribution
data_expon = stats.expon.rvs(scale=1,loc=0,size=1000)

# generate random numbers from Poisson Distribution
data_poisson = stats.poisson.rvs(mu=3, size=10000)

# generate random numbers from Binomial Distribution
data_binom = stats.binom.rvs(n=10,p=0.8,size=10000)

# generate random numbers from Bernoulli Distribution
data_bern = stats.bernoulli.rvs(size=10000,p=0.6)


#plt.plot(pd.DataFrame(data_uniform))

plt.figure()

plt.subplot(231)
plt.hist(pd.DataFrame(data_uniform),50)
plt.title('Uniform')

plt.subplot(232)

plt.hist(pd.DataFrame(data_normal),50)
plt.title('Normal')

plt.subplot(233)

plt.hist(pd.DataFrame(data_expon),50)
plt.title('Exponential')

plt.subplot(234)

plt.hist(pd.DataFrame(data_poisson),50)
plt.title('Poisson')

plt.subplot(235)

plt.hist(pd.DataFrame(data_binom),50)
plt.title('Binomial')

plt.subplot(236)

plt.hist(pd.DataFrame(data_bern),100)
plt.title('Bernoulli')


plt.show()

# -stats.distribution.cdf() is used to determine the probability that an observation drawn 
# from a distribution falls below a specified value (known as the cumulative distribution function).

stats.uniform.cdf(x=2.5,         # Cutoff value (quantile) to check
                  loc=0,         # Distribution start
                  scale=10)      # Distribution end

