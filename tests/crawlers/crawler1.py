# Author      : Zuguang Liu
# Date        : 2018-10-25
# Python Ver  : 3.6
# Description : Test web scrawler for gas buddy sub site

import requests
from bs4 import BeautifulSoup

CRWAL_URL = 'http://www.cincygasprices.com/'


def crawl(url):
	priceLst=[]
	srvLst=[]
	addrLst=[]

	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, "html.parser")
	for priceLink in soup.findAll('div', {'class': 'price_num'}):
		priceLst.append(float(priceLink.string))
	for srvTag in soup.findAll('dt'):
	    srvLst.append(str(srvTag.contents[1].contents[0]))
	for addrTag in soup.findAll('dd'):
		addrStr=str(addrTag.contents[0])
		if addrStr!=' ':
			addrLst.append(addrStr)
	return (len(priceLst), priceLst, srvLst,addrLst)

print(crawl(CRWAL_URL))