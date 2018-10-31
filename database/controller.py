# Author      : Zuguang Liu
# Date        : 2018-10-29 22:40:14
# Python Ver  : 3.6
# Description : 

from query_lib import *
from uszipcode import SearchEngine, Zipcode, state_abbr
import datetime
import sys

def list_transpose(lst):
	check_type(lst,list,'Input must be a list')
	for x in lst:
		check_type(x,list,'An element of the input must be a list')
		if len(x)!= len(lst[0]):
			raise ValueError('Length of each element must be the same')

	return [list(i) for i in zip(*lst)]

def state_zip_by_popdense(state_str,num_returns):
	search = SearchEngine()
	res=search.query(state=state_str,sort_by=Zipcode.population_density, ascending=False,returns=num_returns)
	return [x.zipcode for x in res]

def usa_zip_by_popdense(zip_per_state):
	zip_dict=dict()
	search=SearchEngine()
	state_list=list(state_abbr.STATE_ABBR_SHORT_TO_LONG.keys())
	for state in state_list:
		zip_list=state_zip_by_popdense(state,zip_per_state)
		if zip_list==[]:
			continue
		zip_dict[state]=zip_list
	return zip_dict

TODAY=datetime.datetime.today()

if os.path.exists(TODAY.strftime('%Y-%m-%d')+'.log'):
	raise Exception('Database has been created today,comback tomorrow')
elif today.hour>22:
	raise Exception('It is not safe to request data close to 12 am, come back after 12 am')


old_stdout = sys.stdout
log_file = open(TODAY.strftime('%Y-%m-%d')+'.log','w')
sys.stdout = log_file

for state, zips in usa_zip_by_popdense(10).items():
	print(state, gas_crawl(zips,20).to_csv('gas_'+state))

sys.stdout = old_stdout
log_file.close()