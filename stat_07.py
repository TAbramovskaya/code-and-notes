import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

random_state = 42
rv_norm = stats.norm(100, 20)
sample = rv_norm.rvs(10, random_state=random_state)

# plt.boxplot(sample)

# plt.show()

# print(sample)

rng = np.random.default_rng(42)

a = stats.norm().rvs(size=10, random_state=rng)
b = stats.uniform().rvs(size=10, random_state=rng)
c = stats.chi2(df=5).rvs(size=10, random_state=rng)

# print(a)
# print(b)
# print(c)

# Постройте выборку бета-распределения объемом 2000 с параметрами a=2, b=6, смещением 3 и разбросом 10. Нарисуйте гистограмму для выборки и теоретическую плотность вероятности распределения на одной оси. Какой график ближе к полученную результату?

rv_beta = stats.beta(a=2, b=6, loc=3, scale=10)
sample = rv_beta.rvs(size=2000)

rel_freq = stats.relfreq(sample)
a = rel_freq.lowerlimit + np.arange(rel_freq.frequency.size)*rel_freq.binsize
x = np.linspace(rv_beta.ppf(q=0.01), rv_beta.ppf(q=0.99), 100)

plt.plot(x, rv_beta.pdf(x), 'r-', alpha=1)
plt.bar(a, rel_freq.frequency)
# plt.hist(sample, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

# Определите 1, 55 и 90 процентили этого теоретического бета-распределения.

print(rv_beta.ppf(q=0.01), rv_beta.ppf(q=0.55), rv_beta.ppf(q=0.90))

# Найти значение, больше которого 20% значений распределения, о котором говорили выше. Выберите ответ.

print(rv_beta.ppf(q=0.8))

# Найдите теоретические характеристики распределения. Результат округлите до сотых выпишете через пробел по порядку: среднее медиана дисперсия стандартное отклонение.

print(rv_beta.mean(), rv_beta.median(), rv_beta.var(), rv_beta.std())
