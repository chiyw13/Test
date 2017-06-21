import pandas as pd
import numpy as np
import pylab as pl

df = pd.read_csv('train.csv', header=0)
# for i in range(1,4):
#     print i, len(df[(df['Sex'] == 'male')&(df['Pclass'] == i)])
#
# df['Age'].dropna().hist(bins = 16, range = (0,80), alpha = 0.5)
# pl.show()
# define female=0, male=1
df['Gender'] = df['Sex'].map({'female':0, 'male':1}).astype(int)
print df.head()