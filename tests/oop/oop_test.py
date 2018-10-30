# Author      : Zuguang Liu
# Date        : 2018-10-28 19:37:50
# Python Ver  : 3.6
# Description : 

import requests
from bs4 import BeautifulSoup
import pandas
import os.path
from uszipcode import SearchEngine, Zipcode, state_abbr
import datetime
from custom_lib import *

class GasBuddyQuery(object):
	zipcodes=None
	reqNum=None
	zipLst=[]
	stateLst=[]
	priceLst=[]
	servLst=[]
	addrLst=[]
	_reqDate=datetime.datetime.today()
	_ZIPCODES_ERROR_MSG='zipcodes is not a list of 5-digit strings or a 5-digit string'
	_REQNUM_ERROR_MSG='reqNum is not a integer between 10 and 9990'
	_OTHER_ATTR_NOT_TOUCHABLE='attributes other than inputs cannot be assigned manually'

	def _backdoorSet(self,attrName,value):
		self.__dict__[attrName] = value

	def __setattr__(self, attrName, value):
		if value==None:
			self._backdoorSet(attrName,value)
			return
		if attrName == 'zipcodes':
			if isinstance(value,str):
				if value.isdigit() and len(value)==5:
					self._backdoorSet(attrName,value)
					return
			elif isinstance(value,list):
				if all(isinstance(x, str) for x in value):
					if all(x.isdigit() and len(x)==5 for x in value):
						self._backdoorSet(attrName,value)
						return
			raise AttributeError(self._ZIPCODES_ERROR_MSG)
		elif attrName == 'reqNum':
			if isinstance(value,int):
				if value>9 and value<9990:
					self._backdoorSet(attrName,value)
					return
			raise AttributeError(self._REQNUM_ERROR_MSG)
		else:
			raise AttributeError(self._OTHER_ATTR_NOT_TOUCHABLE)

	def __init__(self,zipcodes=None,reqNum=None):
		self.zipcodes=zipcodes
		self.reqNum=reqNum

	def _simpleCrawl(self,z,n):
		url='https://www.gasbuddy.com/home?search='+z
		for i in range(n//10):
			curl=url+'&cursor='+str(10*i+1)
			source_code = requests.get(curl).text
			soup = BeautifulSoup(source_code, "html.parser")

			for addrTag in soup.findAll('div', {'class': 'styles__address___8IK98'}):
				self.addrLst.append(str(addrTag.contents[0])+', '+str(addrTag.contents[2]))

			for priceTag in soup.findAll('span', {'class': 'styles__price___3DxO5'}):
				self.priceLst.append(str(priceTag.contents[0]))

			for servTag in soup.findAll('h3', {'class': 'style__header3___3T2tm style__header___onURp style__snug___2HJ4K styles__stationNameHeader___24lb3'}):
				self.servLst.append(str(servTag.contents[0]))

	def _cleanLists(self):
		for i in range(len(self.addrLst)):
			if i==0 and self.addrLst[i] in self.addrLst[0:i]:
				self.addrLst[i]=None
				self.priceLst[i]=None
				self.servLst[i]=None
			elif self.priceLst[i]=='---':
				self.addrLst[i]=None
				self.priceLst[i]=None
				self.servLst[i]=None
		self._backdoorSet('addrLst',[x for x in self.addrLst if x is not None])
		self._backdoorSet('priceLst',[float(x[1:]) for x in self.priceLst if x is not None])
		self._backdoorSet('servLst',[x for x in self.servLst if x is not None])

	def crawl(self):
		if self.zipcodes==None or self.reqNum==None:
			raise ValueError('Query inputs not fully defined yet')
		elif isinstance(self.zipcodes,list):
			for onezip in self.zipcodes:
				self._simpleCrawl(onezip,self.reqNum)
		else:
			self._simpleCrawl(self.zipcodes,self.reqNum)
		self._cleanLists()
		return (len(self.priceLst),self.priceLst,self.servLst,self.addrLst)

q=GasBuddyQuery()
q.zipcodes=['45220','44141']
q.reqNum=10
print(q.crawl())
