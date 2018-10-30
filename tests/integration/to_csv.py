# Author      : Zuguang Liu
# Date        : 2018-10-27 20:57:39
# Python Ver  : 3.6
# Description : Test script that outputs gas stations

import pandas
import os.path
from custom_lib import *

def write_to_csv(file_name,row_lst,csv_header):
	check_type(file_name,str,'file_name must be a string')
	check_type(row_lst,list,'rows must be a list of lists')
	check_type(csv_header,list,'header must be a list')
	for row in row_lst:
		check_type(row,list,'each row must be a list')
		if len(row) != len(csv_header):
			raise ValueError('length of each row must be the same as length of the header')

	if file_name[-4:]!='.csv':
		file_name+='.csv'
	pd = pandas.DataFrame(row_lst)
	if os.path.exists(file_name):
		pd.to_csv(file_name, mode='a', index=False, header=False)
	else:
		pd.to_csv(file_name, mode='w', index=False, header=csv_header)
