from scipy import stats 


print(stats.norm.sf(135, loc=100, scale=67))

confidence = 0.95
alpha = 1 - confidence

n = (stats.norm.ppf(1 - alpha / 2) * 15 / 5) ** 2

print(n)