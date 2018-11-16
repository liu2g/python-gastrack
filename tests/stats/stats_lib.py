# Author      : Zuguang Liu
# Date        : 2018-11-15 16:38:39
# Python Ver  : 3.6
# Description : 

import pandas
import datetime
import numpy

df=pandas.read_csv('gas_OH.csv')
df['date']=[datetime.datetime.strptime(x, '%Y-%m-%d') for x in df['date']]
df['city']=[x.split(',')[1].strip() for x in df['address']]
df=df.iloc[0:3]
table=pandas.pivot_table(df,index=['service'], aggfunc=[max])
print(list(table['max']['address']))