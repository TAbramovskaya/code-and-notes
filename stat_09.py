import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


df = pd.read_csv("Salary.csv")
df = df.dropna()

mean_salary_by_education = df.groupby("Уровень образования")["Зарплата"].mean().reset_index()

max_mean_salary = mean_salary_by_education.loc[mean_salary_by_education["Зарплата"].idxmax()]
                                           
print(max_mean_salary)