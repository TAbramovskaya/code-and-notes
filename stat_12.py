import numpy as np
from scipy import stats
import math


# You're analyzing advertising campaigns and their conversion rates. You know that the number of conversions from advertising campaigns per day is distributed uniformly over the interval [0, 12]. You have 10 new campaigns. Model the CLT and see how the average number of conversions is distributed. Find the average conversion rate and the standard error of the mean

rng = np.random.default_rng(42)

uni = stats.uniform(loc=0, scale=12)

population_mean = 6
population_std = 12 / math.sqrt(12)

n = 10
num_experiments = 1000
campaigns = []

for _ in range(num_experiments):
    campaigns.append(
        sum(uni.rvs(size=n, random_state=rng))
    )

campaigns_theoretical_mean = n * population_mean
campains_theoretical_std = math.sqrt(10) * population_std
campaigns_sample_mean = np.mean(campaigns)
csm = sum(campaigns)/ num_experiments
campaigns_sample_std = np.std(campaigns, ddof=1)


print(f"Single campain population: mean={round(population_mean, 4)}, std={round(population_std, 4)}")
print(f"10 cmpaigns theoretical mean={round(campaigns_theoretical_mean, 4)} and std={round(campains_theoretical_std, 4)}")
print(f"10 campaigns sample mean={round(campaigns_sample_mean, 4)} and std={round(campaigns_sample_std, 4)}")
print(f"10 campaigns theoretical standard error={round(campains_theoretical_std / math.sqrt(num_experiments), 6)}")

