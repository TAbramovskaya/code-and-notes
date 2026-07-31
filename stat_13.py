import numpy as np
from scipy import stats
import math


# Find the estimate of the parameters of the uniform distribution ausing bthe method of moments.

sample = [1]*3 + [2]*5 + [5]*6 + [8]*4 + [9]*5
print(np.mean(sample), np.std(sample, ddof=1))

#  (a + b) / 2 = mean
#  (b - a) / sqrt(12) = std

#  b = std * sqrt(12) + a
#  2*a + std * sqrt(12) = 2 * mean
#  a = mean - std * sqrt(3)

a = np.mean(sample) - math.sqrt(3) * np.std(sample, ddof=1)
b = np.std(sample, ddof=1) * math.sqrt(12) + a

print(a, b)

# Confidence intervals

print(stats.norm.ppf(0.99))