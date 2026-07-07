import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Загрузите данные и убедитесь, что всё считалось правильно: посмотреть на столбцы, размер, наличие пропущенных значений (если есть – удалить). Также изучите типы переменных.

df = pd.read_csv("Salary.csv")

print("\n----- Inspect column types and missing values:")                       # Inspect column types and missing values
df.info(verbose=True)   # info() method prints, doesn't return
print("-----")

print("\n----- Rows containing at least one NaN: \n", df.isna().any(axis=1))    # Rows containing at least one NaN
print("\n----- Count NaNs in each column: \n", df.isna().sum())                 # Count NaNs in each column
print("\n----- Count missing values as percentage: \n", 100 * df.isna().mean()) # Count missing values as percentage

print("\n----- Check for duplicate rows: \n", df.duplicated().sum())            # Check for duplicate rows
print("-----")

df = df.dropna()    # Rows with no NaNs

print("\n----- Inspect categorical data for the impossible values: \n", df["Пол"].describe())                       # Inspect data for the impossible 

# print(df.dtypes, df.head(), df.tail(), df.shape)

# Оцените качество выборки, опираясь на распределение данных по полу, по городам, по возрастам, по степени образования. В каких пропорциях присутствуют данные в выборке. Можно ли считать выборку репрезентативной?
 
# Ask:
# Are some categories extremely rare?
# Are there suspicious spikes?
# Are there obvious data entry errors?

print("\n----- Compute summary statistics for numerical columns: \n", df.describe())    # Compute summary statistics for numerical columns

print("\n----- Look at the distribution for numerical variables:")    # Look at the distribution for numerical variables
fig, ax = plt.subplots()
df.hist(figsize=(10, 5), ax=ax)
plt.show()

print("\n----- Compute summary statistics for categorical columns: \n")    
print('\n', df["Пол"].value_counts())
print('\n',df["Регион"].value_counts())
print('\n',df["Уровень образования"].value_counts())

# Постройте плотность распределения для заработной платы для всех данных. Выведите описательные характеристики.

fig, ax = plt.subplots()
df.boxplot(column="Зарплата", ax=ax)
plt.show()

# Identify outliers like those shown in a boxplot

q1 = df["Зарплата"].quantile(0.25)  # 25th percentile (0.25 quantile)
q3 = df["Зарплата"].quantile(0.75)  # 75th percentile (0.75 quantile)

iqr = q3 - q1                       # interquartile range
lower = q1 - 1.5*iqr                # Whiskers: extend to the most extreme points
upper = q3 + 1.5*iqr

outliers = df[(df["Зарплата"] < lower) | (df["Зарплата"] > upper) ]

print("\n----- Describe outliers: \n")    
print(outliers.describe())

print("\n----- Salary description: \n")    
frequency_counts, bin_edges = np.histogram(df["Зарплата"], bins=20, density=True)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
bin_width = bin_edges[1] - bin_edges[0]

fig, ax = plt.subplots()
ax.bar(bin_centers, frequency_counts, width=bin_width, align='center')
ax.set_xticks(bin_centers)
ax.tick_params(axis='x', rotation=45)

plt.show()

print(df["Зарплата"].describe())

# Найдите описательные характеристики для заработной платы с разбивкой по городам и оцените разницу между показателями.

print(df.groupby("Регион").agg(
    min_salary = ("Зарплата", 'min'),
    mean_salary = ("Зарплата", lambda x: round(x.mean(), 2)),
    median_salary = ("Зарплата", lambda x: round(x.median(), 2)),
    max_salary = ("Зарплата", 'max'),
    )
)