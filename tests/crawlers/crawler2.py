# Author      : Zuguang Liu
# Date        : 2018-10-25
# Python Ver  : 3.6
# Description : Test web scrawler for gas buddy main site, one request returns one station

import requests
from bs4 import BeautifulSoup

def crawl(zipcode,num_req):
	url='https://www.gasbuddy.com/home?search='+str(zipcode)

	addrLst=[]
	servLst=[]
	priceLst=[]

	for i in range(num_req):
		curl=url+'&cursor='+str(i)
		source_code = requests.get(curl).text
		soup = BeautifulSoup(source_code, "html.parser")

		addrTag=soup.find('div', {'class': 'styles__address___8IK98'}).contents
		addrStr=str(addrTag[0]+', '+str(addrTag[2]))
		if addrStr in addrLst:
			continue
		addrLst.append(addrStr)

		pricestr=str(soup.find('span', {'class': 'styles__price___3DxO5'}).contents[0])
		if pricestr=='---':
			addrLst.pop(-1)
			continue
		priceLst.append(float(pricestr[1:]))

		servStr=str(soup.find('h3', {'class': 'style__header3___3T2tm style__header___onURp style__snug___2HJ4K styles__stationNameHeader___24lb3'}).contents[0])
		servLst.append(servStr)
	return (len(priceLst),priceLst,servLst,addrLst)

print(crawl(45220,100))