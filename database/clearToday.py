# Author      : Zuguang Liu
# Date        : 2018-11-08 15:20:19
# Python Ver  : 3.6
# Description : 

import csv
import os
import datetime
import glob


def clearToday():
	for file in glob.glob('*.csv'):
		with open(file, 'r') as inp, open(file+'.temp', 'w') as out:
			writer = csv.writer(out)
			for row in csv.reader(inp):
				if row[0] != datetime.datetime.today().strftime('%Y-%m-%d'):
					writer.writerow(row)
		os.remove(file)
		os.rename(file+'.temp', file)

if __name__=="__main__":
	clearToday()