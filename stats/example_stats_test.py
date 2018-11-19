# Author      : Zuguang Liu
# Date        : 2018-11-18 15:23:51
# Python Ver  : 3.6
# Description : 

from stats_lib import *
import sys

ptofile=True

if ptofile:
	# Transfer print window to a log file
	old_stdout = sys.stdout
	log_file = open('stats_report.log','w')
	sys.stdout = log_file

DIR='../database/'

print('***********************************Gas in USA Today***************************************')
print(USGasToday(DIR))
print('*********************************Gas in USA Last Week*************************************')
print(USGasThisWeek(DIR))

stat=gasStats(st='OH',fileName=DIR+'gas_OH.csv')
print('**********************************Price Table in OH***************************************')
print(stat.getPriceTable())
print('********************************Service Analysis in OH************************************')
print(stat.getOtherStats('service'))
print('*********************************Date Analysis in OH**************************************')
print(stat.getOtherStats('date'))
print('*********************************City Analysis in OH**************************************')
print(stat.getOtherStats('city'))

if ptofile:
	sys.stdout = old_stdout
	log_file.close()