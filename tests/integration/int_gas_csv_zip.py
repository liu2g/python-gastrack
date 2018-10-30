# Author      : Zuguang Liu
# Date        : 2018-10-28 05:13:29
# Python Ver  : 3.6
# Description : A test script for integration of gas module and csv module and zipcode module

import requests
from bs4 import BeautifulSoup
from custom_lib import *
import pandas
import os.path
from uszipcode import SearchEngine, Zipcode, state_abbr

GAS_HEADER=['zipcode','state','price','service','address']

def gas_crawl(zipcode,num_req):
	check_type(zipcode,str,'Zipcode must be a string of five digits')
	check_type(num_req,int,'Number of requests must be an integer')
	if not zipcode.isdigit() or len(zipcode)!=5:
		raise ValueError('Zipcode must be a string of five digits')

	if num_req>9990:
		raise ValueError('Gas buddy can only handle less than 9990 requests')

	if num_req<10:
		raise ValueError('Too few requests is not worth searching')

	url='https://www.gasbuddy.com/home?search='+zipcode

	addrLst=[]
	servLst=[]
	priceLst=[]

	for i in range(num_req//10):
		curl=url+'&cursor='+str(10*i+1)
		source_code = requests.get(curl).text
		soup = BeautifulSoup(source_code, "html.parser")

		for addrTag in soup.findAll('div', {'class': 'styles__address___8IK98'}):
			addrLst.append(str(addrTag.contents[0])+', '+str(addrTag.contents[2]))

		for  priceTag in soup.findAll('span', {'class': 'styles__price___3DxO5'}):
			priceLst.append(str(priceTag.contents[0]))

		for servTag in soup.findAll('h3', {'class': 'style__header3___3T2tm style__header___onURp style__snug___2HJ4K styles__stationNameHeader___24lb3'}):
			servLst.append(str(servTag.contents[0]))
	
	for i in range(len(addrLst)):
		if i==0 and addrLst[i] in addrLst[0:i]:
			addrLst[i]=None
			priceLst[i]=None
			servLst[i]=None
		elif priceLst[i]=='---':
			addrLst[i]=None
			priceLst[i]=None
			servLst[i]=None
	addrLst=[x for x in addrLst if x is not None]
	priceLst=[float(x[1:]) for x in priceLst if x is not None]
	servLst=[x for x in servLst if x is not None]

	return (len(priceLst),priceLst,servLst,addrLst)

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

def make_gas_database(num_zip_per_state,num_stations,csv_name='usa_gas.csv'):
	reqZipTable=usa_zip_by_popdense(num_zip_per_state)
	for aZip in reqZipTable:
		thisNumSta,thisPriceLst,thisServLst,thisAddrLst=gas_crawl(aZip[0],num_stations)
		thisZipLst=[aZip[0]]*thisNumSta
		thisStateLst=[aZip[1]]*thisNumSta
		this_row_lst=list_transpose([thisZipLst,thisStateLst,thisPriceLst,thisServLst,thisAddrLst])
		write_to_csv(csv_name,this_row_lst,GAS_HEADER)

make_gas_database(1,10)