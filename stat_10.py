import math
from scipy.stats import norm


# 10.2 p326 Students' weights example 

mu_null = 68
sigma = 3.6
n = 64

sigma_mu = sigma / math.sqrt(n)
z = (67 - 68) / sigma_mu

alpha = round(2 * norm.cdf(z), 6)

print("Type I error probability: ", alpha, " -- reject H0 when the average weight is actually 68")

print("calculated without z-value correction: ", round(2*norm.cdf(67, loc=mu_null, scale=sigma_mu), 6))

mu_a = 70
z_a_left = (67 - 70) / sigma_mu 
z_a_right = (69 - 70) / sigma_mu
beta = norm.cdf(z_a_right) - norm.cdf(z_a_left)

print("Type II error probability: ", round(beta, 6))

print(2 * norm.cdf(-2.73))