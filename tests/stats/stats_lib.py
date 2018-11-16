# Author      : Zuguang Liu
# Date        : 2018-11-15 16:38:39
# Python Ver  : 3.6
# Description : 

import pandas
import datetime

df=pandas.read_csv('gas_OH.csv')
df['date']=[datetime.datetime.strptime(x, '%Y-%m-%d') for x in df['date']]
df['address']=[x.split(',')[1].strip() for x in df['address']]
print(df.describe())