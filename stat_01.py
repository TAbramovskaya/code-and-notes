import pandas as pd
import numpy as np
import random
out_file = "stat_out.csv"


df = pd.read_csv("itresume-coderun.csv")

sample = df.sample(15)

N = 1000
stratified_proportional = df.groupby('problem_id', group_keys=False).apply(lambda x: x.sample(int(np.rint(N*len(x)/len(df)))))

users = pd.read_csv("itresume-users.csv")

users['period'] = pd.to_datetime(users["date_joined"]).dt.to_period("Q").apply(lambda x: x.strftime('%F-Q%q'))

print(users.groupby("period").count())

clusters = users["period"].drop_duplicates().sample(2)

clusters2 = random.sample(users['period'].unique().tolist(), 2)
print(clusters2)    
clusters.to_csv(out_file)

serial_sample = users[users['period'].isin(clusters)]
print(serial_sample)

cluster_sample = serial_sample.groupby('period', group_keys=False).apply(lambda x: x.sample(frac=0.7))
