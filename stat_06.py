import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rv = stats.norm(loc=2, scale=8)
sample = rv.rvs(1000)

cum_freq = stats.cumfreq(sample, numbins=25)
rel_freq = stats.relfreq(sample, numbins=25)
# rel_freq = stats.relfreq(sample, numbins=25, defaultreallimits=(sample.min(), sample.max()))

print(cum_freq.lowerlimit == rel_freq.lowerlimit)

a = cum_freq.lowerlimit + np.arange(cum_freq.cumcount.size) * cum_freq.binsize

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.hist(sample, bins=25)
ax2.bar(a, cum_freq.cumcount, width=cum_freq.binsize)
ax3.bar(a, rel_freq.frequency, width=rel_freq.binsize)

plt.show()
