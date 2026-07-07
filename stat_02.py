# Сформируйте кластеризованную выборку из 20 пользователей из таблицы USERS так, чтобы в нее входили клиенты из 3 случайных компаний (company_id) в таких же пропорциях, как они представлены в генеральной совокупности. 

# Далее на основании этой кластерной выборки клиентов сформируйте стратифицированную выборку для таблицы CODERUN таким образом, чтобы в нее входило по 1 случайной строке для каждой даты (created_at).

import pandas as pd
import math
import numpy as np


users = pd.read_csv("itresume-users.csv")

companies = users["company_id"].drop_duplicates().sample(3)
users_flt = users[users["company_id"].isin(companies)]
 
# company_stat = users_flt.groupby("company_id").size().reset_index(name="num_users")

# company_stat["fraction"] = company_stat["num_users"] / len(users_flt)
# print(company_stat)

N = 20
clustered = users_flt.groupby("company_id", group_keys=False).apply(lambda x: x.sample(math.floor(N*len(x)/len(users_flt)), replace=True))
clustered.to_csv("stat_out.csv")


coderun = pd.read_csv("itresume-coderun.csv")
coderun["date"] = pd.to_datetime(coderun["created_at"]).dt.date
day_run = coderun[coderun["user_id"].isin(clustered["id"])].groupby("date").apply(lambda x: x.sample(1))

print(day_run)

