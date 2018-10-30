# Author      : Zuguang Liu
# Date        : 2018-10-27 19:17:08
# Python Ver  : 3.6
# Description : Test web scrawler for gas buddy main site, one request returns ten stations

import requests
from bs4 import BeautifulSoup
from custom_lib import *

def gas_crawl(zipcode,num_req):
	check_type(zipcode,str,'Zipcode must be a string of five digits')
	check_type(num_req,int,'Number of requests must be an integer')
	if not zipcode.isdigit() or len(zipcode)!=5:
		raise ValueError('Zipcode must be a string of digits')

	if num_req>9990:
		raise ValueError('Gas buddy can only handle less than 9990 requests')

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


print(gas_crawl('45220',100))