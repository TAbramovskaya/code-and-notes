import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


np_sample = np.random.uniform(2, 8, 1000)

rv = stats.uniform
sample = rv.rvs(loc=2, scale=6, size=1000) # random variates sample

cum_freq = stats.cumfreq(sample, numbins=25)
rel_freq = stats.relfreq(sample, numbins=25)

print(cum_freq)
print(rel_freq)

x = cum_freq.lowerlimit + np.linspace(0, cum_freq.binsize*cum_freq.cumcount.size, cum_freq.cumcount.size)
a = cum_freq.lowerlimit + np.arange(cum_freq.cumcount.size) * cum_freq.binsize
b = rel_freq.lowerlimit + np.arange(rel_freq.frequency.size) * rel_freq.binsize
print(x)
print(a)
print(b) # a and b are equal

# fig = plt.figure()

# ax1 = fig.add_subplot(1, 4, 1)
# ax2 = fig.add_subplot(1, 4, 2)
# ax3 = fig.add_subplot(1, 4, 3)
# ax4 = fig.add_subplot(1, 4, 4)

# ax1.hist(sample, bins=25)

# ax2.bar(x, cum_freq.cumcount, width=cum_freq.binsize)

# ax3.bar(a, cum_freq.cumcount, width=cum_freq.binsize)

# ax4.step(a, cum_freq.cumcount)

# plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(1, 1, 1)
ax.bar(a, rel_freq.frequency)

plt.show()
