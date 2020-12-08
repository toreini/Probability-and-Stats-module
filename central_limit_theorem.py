#A simulation to explain Central Limit Theorem: 
# even when a sample is not normally distributed, if you draw multiple samples and take each of their averages,
#  these averages will represent a normal distribution.


#in an e-commerce shop, most of our customers are non-buying customers. 
# So the distribution actually looks like an exponential, and since a Poisson can be derived from an exponential, 
# let’s make some exponential distributions to reflect our customers’ purchases.

#Let us assume our customer base has an average order value of $170, 
# so we will create exponential distributions with this average. 
# We will attempt to get this value by looking at some sample averages.


#I draw a sample of 1000 customers. Then repeat this 4 times. I get the following four distributions 
# (To get graphs similar to this, use the code at the end with repeat_sample_draws_exponential(4, 1000, 170, True) )


import numpy as np
import matplotlib.pyplot as plt

def repeat_sample_draws_exponential(n, samp_size, mu, show_all=False):
    means = []

    samples = []
    for ii in range(0, n):
        samples.append(np.random.exponential(mu, samp_size))
        means.append(np.mean(samples[ii]))

    if show_all:
        pltdim = np.math.ceil(np.math.sqrt(n))
        fig, axs = plt.subplots(pltdim, pltdim, figsize=(8, 8), gridspec_kw={'hspace': 0.2}, sharex=True, sharey=True)
        fig.suptitle('Individual Samples\' Order Value Distribution')
        fig.text(0.5, 0.04, 'Order Values ($)', ha='center')
        fig.text(0.04, 0.5, 'Number of Customers', ha='center', rotation='vertical')
        axs = axs.flatten()
        for ii in range(0, n):

            plt.sca(axs[ii])

            plt.gca().hist(samples[ii], bins=int(50), histtype='step',
                           label='$mean = {0:.2f}$'.format(np.mean(samples[ii])), range=[0, 2 * mu])
            if n < 10:
                plt.gca().set_title('Sample #{0} : average={1:.2f}'.format(ii, np.mean(samples[ii])))
            for item in ([axs[ii].title, axs[ii].xaxis.label, axs[ii].yaxis.label] +
                             axs[ii].get_xticklabels() + axs[ii].get_yticklabels()):
                item.set_fontsize(8)

        plt.savefig('expdist_{0}_mu_{1}_sample_{2}_sampsize'.format(mu, n, samp_size))

    plt.clf()
    plt.hist(means, bins=int(10), histtype='step')
    plt.title('Overall Average of {} Samples\' Average Order Value'.format(n))
    plt.xlabel('Average of Individual Sample\'s Order Value ($)')
    plt.savefig('average_of_expdist_{0}_mu_{1}_sample_{2}_sampsize'.format(mu, n, samp_size))
    print('mean of the samples is {0:.2f}'.format(np.mean(means)))
    print('standard deviation of the samples is {0:.2f}'.format(np.std(means)))

repeat_sample_draws_exponential(100, 1000, 170, True)