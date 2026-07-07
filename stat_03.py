from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np


df = 10

x = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 10)
pdf_chi2 = chi2.pdf(x, df)

vals = chi2.ppf([0.001, 0.5, 0.999], df)
print(np.allclose([0.001, 0.5, 0.999], chi2.cdf(vals, df)))

r = chi2.rvs(df, size=1000)

fig, ax = plt.subplots(1, 1)
ax.plot(x, chi2.pdf(x, df), 'r-', lw=5, alpha=0.2, label='chi2 pdf')
ax.hist(r, density=True, bins='auto', histtype='stepfilled', alpha=0.8)
ax.set_xlim(x[0], x[-1])
ax.legend(loc='best', frameon=False)

plt.show()
