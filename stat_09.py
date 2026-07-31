import pandas as pd
import numpy as np
from scipy.stats import binom, norm
import matplotlib.pyplot as plt
import math

#  10.2 p321 Vaccine example

n = 100
p = 0.25
p_a = 0.5
k = 36

print("Binomial: ")
alpha = binom.sf(k, n, p)
beta = binom.cdf(k, n, p_a)

print("\tType I error probability: ", round(alpha, 6))
print("\tType II error probability: ", round(beta, 6))

print("Normal approximation: ")
mu = n*p
sigma = math.sqrt(mu*(1 - p))

print("\tNull mu and sigma: ", mu, sigma)

z = (36.5 - mu) / sigma
alpha_norm = norm.sf(z)

print("\tType I error probability: ", round(alpha_norm, 6))

mu_a = n * p_a
sigma_a = math.sqrt(mu_a * (1 - p_a))

print("\tAlternative mu and sigma: ", mu_a, sigma_a)
beta_norm = norm.cdf((36.5 - mu_a) / sigma_a)

print("\tType II error probability: ", round(beta_norm, 6))