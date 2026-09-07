import numpy as np
from scipy import stats
import math


# Find the estimate of the parameters of the uniform distribution using the method of moments.

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

# Let n = 25, the mean calculated for the sample size be 130. The standard deviation is known from previous studies σ = 12. Construct a 97% confidence interval for the mean. Round your answer to hundredths.

confidence = 0.97
alpha = 1 - confidence

mean = 130
std = 12
n = 25

z = stats.norm.ppf(1 - alpha / 2)

delta = std * z / math.sqrt(n)
interval = (mean - delta, mean + delta)

print(interval)


# Find the minimum sample size required to construct an interval estimate of the mean with an accuracy of ∆ = 3, a variance of 400, and a confidence level of 0.95

delta = 3
var = 400
confidence = 0.95

alpha = 1 - confidence
z = stats.norm.ppf(1 - alpha / 2)

n = z * z * var / (delta * delta)

print(n)


# A sample of 19 firms was compiled for the industry. The sample standard deviation for the number of employees per firm was found to be 25. Construct a 90% confidence interval for the standard deviation of the number of employees in a firm for this industry. What is the maximum deviation from the mean given these parameters?

n = 19
std = 25

confidence = 0.9
alpha = 1 - confidence

chi2_left = stats.chi2.ppf(1 - alpha / 2, df=n-1)
chi2_right = stats.chi2.ppf(alpha / 2, df=n-1)

interval = ((n-1)*std**2 / chi2_left, (n-1)*std**2 / chi2_right)

print(interval)
print(math.sqrt(interval[1]))


# Over the past 5 years, the annual price growth of asset A averaged 20% with a standard deviation of 5%. Construct a confidence interval with a significance level of 0.05 for the asset's price at the end of next year if it starts at $100.

n = 5
std = 0.05
mean = 0.2

alpha = 0.05
delta = std * math.sqrt(1 + 1/n) * stats.t.ppf(1 - alpha / 2, n - 1)

cur_price = 100
interval = (cur_price * (1 + (mean - delta)), cur_price * (1 + (mean + delta)))

print(interval)


# We ran a marketing campaign and collected data on the number of purchases over 50 days. We recorded the number of sales in a sales ledger every day. The data showed that we had an average of 10 purchases per day, with a standard deviation of 5. There are five days left until the end of the month, and we still need 60 sales to reach our plan. Do we have a 95% chance of reaching our plan?

confidence = 0.99
alpha = 1 - confidence

n = 50
mean_1d = 10
std_1d= 5

days = 5
mean = days * mean_1d
std = math.sqrt(days) * std_1d

prob_geq_60 = stats.norm.sf(60, loc=mean, scale=std)

prediction_interval = (
    stats.norm.ppf(alpha / 2, loc=mean, scale=std), 
    stats.norm.ppf(1 - alpha / 2, loc=mean, scale=std)
)

print(prob_geq_60)
print(prediction_interval)

quantile = stats.norm.ppf(1 - alpha / 2)
delta = std_1d * quantile / math.sqrt(n)
print(f'95% confidence interval for 1 day average: ({mean_1d - delta}, {mean_1d + delta})' )

# # Confidence interval: (8.614096175650323, 11.385903824349677)
# Let's multiply by 5:
# (43.070480878251615, 56.929519121748385)
# This means that there is a 95% chance that the store will not be able to fulfill its plan.


# A company is launching a marketing campaign to promote its product. We want to determine the optimal sample size needed to survey potential customers and evaluate the campaign's effectiveness. We have previous data on product awareness, the standard deviation is 10%, and the expected improvement is 5%. Let's assume the confidence coefficient corresponds to 99% of measurements. What should be the minimum representative sample size?

std = 0.1
mean = 0.05
confidence = 0.99
alpha = 1 - confidence

print((stats.norm.ppf(1 - alpha / 2) * std / mean) ** 2)

# The study surveyed 1,000 people. Of these, 20% expressed interest in the new product. Calculate the sampling error (the confidence level is 95%).

n = 1000
p = 0.2
confidence = 0.95
alpha = 1 - confidence

print(math.sqrt((p * (1 - p)) / n) * stats.norm.ppf(1 - alpha / 2))


# From a customer base of 23,000, 800 people were selected for the study. The average purchase amount (average bill) at a well-known retail chain was determined for each person. The average bill was 500 rubles. The maximum average bill was 2,650 rubles, and the minimum was 220 rubles. Calculate the sampling error (confidence level is 97.5%).

population_size = 23_000
sample_size = 800
mean = 500
max_bill = 2_650
min_bill = 220
confidence = 0.975
alpha = 1 - confidence

sample_range = (max_bill - min_bill) / 5

standard_error = sample_range / math.sqrt(sample_size)

standard_error = sample_range / math.sqrt(sample_size)

finite_population_correction = math.sqrt((population_size - sample_size) / population_size)

error_ = stats.norm.ppf(1 - alpha / 2) * standard_error * finite_population_correction


print(error_)


# An analyst at a vegetarian food ordering service decided to analyze the average income level of its customers to calculate the optimal subscription price. He took a sample of 31 users, calculated the sample mean = 72 and standard deviation = 48. Next, I estimated the average salary value for the general population by constructing a 90% confidence interval. Are the results of this study representative?

n = 31
mean = 72
std = 48
confidence = 0.9
alpha = 1 - confidence

standard_error = std / math.sqrt(n)
margin_of_error = stats.norm.ppf(1 - alpha / 2) * standard_error

interval = (mean - margin_of_error, mean + margin_of_error)

relative_precision = margin_of_error / mean

print(margin_of_error)
print(relative_precision)
print(interval)


# Calculate what the minimum sample size should have been in the previous task, given the error of 10% of the mean?

margin_of_error = mean*0.1

n_desired = (stats.norm.ppf(1 - alpha / 2) * std / margin_of_error)**2

print(n_desired)