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

# Проанализируйте качественный признак "Пол". Какую долю в выборке составляют женщины?
print((df["Пол"] == "женский").mean())  # Don't forget drop NaNa, otherwithe NaNs will be included in the denominator (since NaN == "женский" evaluates to False)

print(df['Пол'].value_counts(normalize=True))


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


print("\n----- Compute summary statistics Salary column: \n", df["Зарплата"].describe())    
print("median ", df["Зарплата"].median())   # compare mean from the above with the median


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


# Есть ли выбросы у признака "Возраст"? Чему примерно равен межквартильный размах?

sex_q1 = df["Возраст"].quantile(0.25)
sex_q3 = df["Возраст"].quantile(0.75)
sex_iqr = sex_q3 - sex_q1

print("\n----- Interquartile range for the Age column: ", sex_iqr)


# Найдите описательные характеристики для заработной платы с разбивкой по городам и оцените разницу между показателями.

print(df.groupby("Регион").agg(
    min_salary = ("Зарплата", 'min'),
    mean_salary = ("Зарплата", lambda x: round(x.mean(), 2)),
    median_salary = ("Зарплата", lambda x: round(x.median(), 2)),
    max_salary = ("Зарплата", 'max'),
    )
)

# For the Moscow:
print("\n----- For the Moscoy city 0.75 quantile: ", df[df["Регион"] == "Москва"]["Зарплата"].quantile(0.75))

# Определите моду для переменной «Опыт работы».

print("\n----- Mode for the Work Experience column: ")

counts = df["Опыт работы"].value_counts()
print("Mode: ", counts.index[0])
print("Frequency: ", counts.iloc[0])


# Определите моду для переменной «Профессия» для городов: Москва, Санкт-Петербург, Омск и Казань.

print("\n----- Experience and Professons in the selected regions: ")

regions = {"Москва", "Санкт-Петербург", "Омск", "Казань"}
print("Rigions: ", regions)

filtered = df[df["Регион"].isin(regions)]

print(filtered.groupby("Регион").agg(
    work_experience_mode = ('Опыт работы', lambda x: x.mode()),
    popular_professions = ('Профессия', lambda x: x.value_counts().idxmax()),
    popular_professions_mode = ('Профессия', lambda x: x.mode().tolist())
    )
)



# Определите для какого уровня образования средняя зарплата по всем регионам выше?
print("\n----- Mean salary exploration: ")

mean_salary_by_education = df.groupby("Уровень образования")["Зарплата"].mean().reset_index()
max_mean_salary = mean_salary_by_education.loc[mean_salary_by_education["Зарплата"].idxmax()]
                                           
print(mean_salary_by_education)
print(max_mean_salary)


# Какой уровень образования представлен в выборке в наибольшем количестве?

print("\n----- The most frequent education level: \n", df['Уровень образования'].value_counts())


# Как распределена средняя зарплата мужчин по профессиям?

df_m = df[df["Пол"] == "мужской"]
mean_salary_men = df_m.groupby("Профессия")["Зарплата"].mean()

fig, ax = plt.subplots()

ax.bar(mean_salary_men.index, mean_salary_men.values.flatten())
ax.tick_params(axis='x', rotation=90)

plt.show()


# В каком регионе медианное значение зарплаты для женщин является наименьшим? 

df_w = df[df["Пол"] == "женский"]

median_salary_women = df_w.groupby("Профессия")["Зарплата"].quantile(0.50)
# median_salary_women = df_w.groupby("Профессия")["Зарплата"].median()

print("\n----- Min median across women by professions: ", median_salary_women.min())

median_salary_women = df_w.groupby("Регион")["Зарплата"].quantile(0.50)
# median_salary_women = df_w.groupby("Профессия")["Зарплата"].median()

print("\n----- Min median across women by region: ", median_salary_women.idxmin())


# Визуализируйте среднюю зарплату в Екатеринбурге по уровню образования для следующих возрастных промежутков: до 19, от 20 до 30, от 31 до 45, от 45 до 60, после 60. При каких условиях можно получать максимальную среднюю зарплату?


ekb = df[df["Регион"] == "Екатеринбург"]
bins = [0, 19, 30, 45, 60, 100]
labels = ["<=19", "20-30", "31-45", "46-60", "61+"]

ekb["Возрастной период"] = pd.cut(ekb["Возраст"], bins=bins, labels=labels)

grouped = (
    ekb.groupby("Возрастной период")["Зарплата"]
        .mean()
)

fig, ax = plt.subplots()

ax.bar(grouped.index, grouped.values)
plt.show()

# Grouped by education level


ekb = df[df["Регион"] == "Екатеринбург"]
bins = [0, 19, 30, 45, 60, 100]
labels = ["<=19", "20-30", "31-45", "46-60", "61+"]

ekb["Возрастной период"] = pd.cut(ekb["Возраст"], bins=bins, labels=labels)

grouped = (
    ekb.groupby(["Возрастной период", "Уровень образования"])["Зарплата"]
        .median()
)

# Matplotlib doesn't know how to plot a MultiIndex directly. 
# Option 1: Convert the index to strings
labels = [
    f"{age}\n{edu}"
    for age, edu in grouped.index
]

fig, ax = plt.subplots()
ax.bar(labels, grouped.values)
ax.tick_params(axis='x', rotation=90)


# Option 2: Use unstack() for a grouped bar chart
grouped = (
    ekb.groupby(["Возрастной период", "Уровень образования"])["Зарплата"]
       .median()
       .unstack()
)

grouped.plot(kind="bar")
plt.show()
