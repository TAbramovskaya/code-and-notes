import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


df = pd.read_csv("Salary.csv")
df = df.dropna()

# Визуализируйте среднюю зарплату в Екатеринбурге по уровню образования для следующих возрастных промежутков: до 19, от 20 до 30, от 31 до 45, от 45 до 60, после 60. При каких условиях можно получать максимальную среднюю зарплату?

ekb = df[df["Регион"] == "Екатеринбург"]

ekb_mean_salary = ekb.groupby("Уровень образования")["Зарплата"].mean()
bins = [20, 30, 45, 60]

plt.hist(ekb_mean_salary, bins=bins)
plt.show()