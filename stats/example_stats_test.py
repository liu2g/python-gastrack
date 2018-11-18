# Author      : Zuguang Liu
# Date        : 2018-11-18 15:23:51
# Python Ver  : 3.6
# Description : 

from stats_lib import *

DIR='../database/'

print('***********************************Gas in USA Today***************************************')
print(USGasToday(DIR))
print('*********************************Gas in USA Last Week*************************************')
print(USGasThisWeek(DIR))

stat=gasStats(st='OH',fileName=DIR+'gas_OH.csv')
print('********************************Service Analysis in OH************************************')
print(stat.getOtherStats('service'))
print('*********************************Date Analysis in OH**************************************')
print(stat.getOtherStats('date'))
print('*********************************City Analysis in OH**************************************')
print(stat.getOtherStats('city'))