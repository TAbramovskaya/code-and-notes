# Загрузите файлы в датафреймы Pandas и назовите их coderun и users. Далее создайте новый датафрейм df, который получается в результате:

# Объединения двух датафреймов по полям с пользователем
# Если для каких-то кодранов не найдена пара в таблице users, такие записи нужно все равно оставить в результирующей таблице
# Если есть совпадающие названия столбцов, то у них в результате должны быть суффиксы _run и _user
# Далее выполните действия:

# Создайте новый датафрейм df2, который будет хранить информацию о том, сколько дней прошло между последним выполнением кода конкретного юзера и днем его регистрации. Столбец с разницей должен называться diff.
# Округлите diff до ближайшего меньшего числа, кратного 50. Результат должен остаться целым числом.
# Создайте датафрейм df3, в который запишите количество юзеров, сгруппированных по разнице дней.
# Результат отсортируйте по убыванию количества user_id.

import pandas as pd
import numpy as np


coderun = pd.read_csv('itresume-coderun.csv')
users = pd.read_csv('itresume-users-pandas.csv', sep=';', skiprows=1)

df = coderun.merge(users, how='left', left_on='user_id', right_on='id', suffixes=('_run', '_user'))

df_ = df.copy()
df_['created_at'] = pd.to_datetime(df_['created_at'])
df_['date_joined'] = pd.to_datetime(df_['date_joined'])

# Transform date_joined, if NA, to the minimum of the created_at
# df['date_joined'] = df['date_joined'].fillna(df.groupby('user_id')['created_at'].transform('min'))

df_ = df_.assign(
    diff=((df_['created_at'] - df_['date_joined']).dt.days // 50) * 50
)

df2 = df_.groupby('user_id')['diff'].agg('max').reset_index(name='diff')
df2 = df2.astype({'user_id': 'Int64', 'diff': 'Int64'})

df3 = df2.groupby('diff', dropna=False)['user_id'].nunique().reset_index(name='user_count')
df3 = df3.astype({'user_count': 'Int64', 'diff': 'Int64'})

df3 = df3.sort_values(by='user_count', ascending=False)

