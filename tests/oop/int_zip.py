# Author      : Zuguang Liu
# Date        : 2018-10-29 22:40:14
# Python Ver  : 3.6
# Description : 

from oop_test2 import *
from uszipcode import SearchEngine, Zipcode, state_abbr
from custom_lib import *

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

for state, zips in usa_zip_by_popdense(10).items():
	print(state, gas_crawl(zips,10).to_csv(state+'_gas'))