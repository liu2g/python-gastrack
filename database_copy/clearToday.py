# Author      : Zuguang Liu
# Date        : 2018-11-08 15:20:19
# Python Ver  : 3.6
# Description : 

import csv
import os
import datetime
import glob

TODAY=datetime.datetime.today()

for file in glob.glob('*.csv'):
	with open(file, 'r') as inp, open(file+'.temp', 'w') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
			if row[0] != TODAY.strftime('%Y-%m-%d'):
				writer.writerow(row)
	os.remove(file)
	os.rename(file+'.temp', file)