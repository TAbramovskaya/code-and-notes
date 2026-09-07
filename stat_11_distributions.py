import numpy as np
import scipy.stats as stats


x = np.array([[25.11, 30.10, np.nan, 32.02, 43.15],
              [14.95, 16.06, 121.25, 94.35, 29.81]])
z_0 = stats.zscore(x, axis=0, nan_policy='omit')    # along columns
# [[ 1.  1. nan -1.  1.]
#  [-1. -1. nan  1. -1.]]
print(z_0)

z_1 = stats.zscore(x, axis=1, nan_policy='omit')    # along rows
# [[-1.13490897 -0.37830299         nan -0.08718406  1.60039602]
#  [-0.91611681 -0.89090508  1.4983032   0.88731639 -0.5785977 ]]
print(z_1)


# You've run your calculations and found that the platform's LTV is normally distributed with a mean of 15,600 and a standard deviation of 5,000. What percentage of users have an LTV between 10,000 and 20,000? Round your answer to the nearest whole number.

mu = 15.6
sigma = 5
print(stats.norm.cdf(20, loc=mu, scale=sigma) - stats.norm.cdf(10, loc=mu, scale=sigma))


# What is the probability that a random variable with a normal distribution μ = 50and   сигма = 10, will be between 30 and 70?

mu = 50
sigma = 10
print(stats.norm.cdf(70, loc=mu, scale=sigma) - stats.norm.cdf(30, loc=mu, scale=sigma))


# What is the probability that a random variable with a standard normal distribution will be less than -1.96

print(stats.norm.cdf(-1.96))


#  What is the probability that a random variable with a standard normal distribution will be greater than 1.645?

print(stats.norm.sf(1.645))


# You're analyzing advertising campaigns and their conversion rates. You know that the number of conversions from advertising campaigns per day is distributed uniformly over the interval [0, 12]. You have 10 new campaigns. Model the CLT and see how the average number of conversions is distributed. Find the average conversion rate and the standard error of the mean

rng = np.random.default_rng(42)

uni = stats.uniform(loc=0, scale=12)
sample = uni.rvs(size=1000)

print(sample.mean())


