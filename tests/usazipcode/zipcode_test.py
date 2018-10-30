# Author      : Zuguang Liu
# Date        : 2018-10-27 19:23:41
# Python Ver  : 3.6
# Description : Test script that uses uszipcode module

from custom_lib import *
from uszipcode import SearchEngine, Zipcode, state_abbr

def state_zip_by_popdense(state_str,num_returns):
	search = SearchEngine()
	res=search.query(state=state_str,sort_by=Zipcode.population_density, ascending=False,returns=num_returns)
	return [x.zipcode for x in res]

def usa_zip_by_popdense(zip_per_state):
	zip_table=[]
	search=SearchEngine()
	state_list=list(state_abbr.STATE_ABBR_SHORT_TO_LONG.keys())
	for state in state_list:
		zip_list=state_zip_by_popdense(state,zip_per_state)
		if zip_list==[]:
			continue
		temp_slist=[state]*zip_per_state
		zip_table.extend(list_transpose([zip_list,temp_slist]))
	return zip_table

print(usa_zip_by_popdense(1))