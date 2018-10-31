# Author      : Zuguang Liu
# Date        : 2018-10-29 20:13:35
# Python Ver  : 3.6
# Description : 

import requests
from bs4 import BeautifulSoup
import pandas
import os.path
import datetime


def gas_crawl(zipcodes,numReq):
	if (isinstance(zipcodes, str) or isinstance(zipcodes,list))==False:
		raise TypeError('zipcodes must be a string or list')
	if isinstance(zipcodes,str):
		if zipcodes.isdigit()==False or len(zipcodes)!=5:
			raise ValueError('zipcodes can only be a 5-digit string')
		else:
			zipcodes=[zipcodes]
	else:
		for x in zipcodes:
			if not isinstance(x,str):
				raise TypeError('Each member of zipcodes list must be a string')
			elif x.isdigit==False or len(x)!=5:
				raise ValueError('Each member of zipcodes must be a 5-digit string')

	if not isinstance(numReq,int):
		raise TypeError('numReq must be an integer')
	elif numReq<10 or numReq>9990:
		raise ValueError('numReq must be an integer between 0 and 9990')

	Q=GasBuddyQuery()

	for onezip in zipcodes:
		url='https://www.gasbuddy.com/home?search='+onezip
		for i in range(numReq//10):
			curl=url+'&cursor='+str(10*i+1)
			source_code = requests.get(curl).text
			soup = BeautifulSoup(source_code, "html.parser")

			for addrTag in soup.findAll('div', {'class': 'styles__address___8IK98'}):
				Q.addrLst.append(str(addrTag.contents[0])+', '+str(addrTag.contents[2]))

			for  priceTag in soup.findAll('span', {'class': 'styles__price___3DxO5'}):
				Q.priceLst.append(str(priceTag.contents[0]))

			for servTag in soup.findAll('h3', {'class': 'style__header3___3T2tm style__header___onURp style__snug___2HJ4K styles__stationNameHeader___24lb3'}):
				Q.servLst.append(str(servTag.contents[0]))
	
	for i in range(len(Q.addrLst)):
		if i==0 and Q.addrLst[i] in Q.addrLst[0:i]:
			Q.addrLst[i]=None
			Q.priceLst[i]=None
			Q.servLst[i]=None
		elif Q.priceLst[i]=='---':
			Q.addrLst[i]=None
			Q.priceLst[i]=None
			Q.servLst[i]=None
	Q.addrLst=[x for x in Q.addrLst if x is not None]
	Q.priceLst=[float(x[1:]) for x in Q.priceLst if x is not None]
	Q.servLst=[x for x in Q.servLst if x is not None]
	Q._readOnly=True

	return Q

class GasBuddyQuery(object):
	_readOnly=False
	def __init__(self):
		self.priceLst=[]
		self.servLst=[]
		self.addrLst=[]
		self.reqDate=datetime.datetime.today()

	def __setattr__(self, attrName, value):
		if self._readOnly==False:
			self.__dict__[attrName] = value
		else:
			raise AttributeError('GasBuddyQuery is a immutable class')

	def transpose(self,lst):
		if not isinstance(lst,list):
			raise TypeError('transpose input must be a list')
		for x in lst:
			if not isinstance(x, list):
				raise TypeError('each member of the input list must be a list')
			if len(x)!= len(lst[0]):
				raise ValueError('length of each member must be the same')

		return [list(i) for i in zip(*lst)]

	def getCheapest(self,rowformat=True):
		cheapIndex=[i for i, x in enumerate(self.priceLst) if x == min(self.priceLst)]
		cols=[[self.priceLst[i] for i in cheapIndex],[self.servLst[i] for i in cheapIndex],[self.addrLst[i] for i in cheapIndex]]
		if rowformat:
			return self.transpose(cols)[0]
		else:
			return cols

	def getAvg(self):
		if self.priceLst==[]:
			return None
		else:	
			return round(sum(self.priceLst)/len(self.priceLst),2)

	def getTable(self,rowformat=True,useDate=False):
		table=[self.priceLst,self.servLst,self.addrLst]
		if useDate:
			table.insert(0,[self.reqDate.strftime('%Y-%m-%d')]*len(self.priceLst))
		if rowformat:
			return self.transpose(table)
		else:
			return table

	def sorted(self):
		old_table=self.getTable()
		new_table=sorted(old_table,key=lambda l:l[0], reverse=False)
		new_table_trans=self.transpose(new_table)
		Q=GasBuddyQuery()
		Q.priceLst=new_table_trans[0]
		Q.servLst=new_table_trans[1]
		Q.addrLst=new_table_trans[2]
		Q._readOnly=True
		return Q

	def removeServ(self,selServ):
		if (isinstance(selServ, str) or isinstance(selServ,list))==False:
			raise TypeError('selServ must be a string or list')
		if isinstance(selServ,str):
			selServ=[selServ]
		else:
			for x in selServ:
				if not isinstance(x,str):
					raise TypeError('Each member of selServ must be a string')

		Q=GasBuddyQuery()

		Q.priceLst=self.priceLst[:]
		Q.servLst=self.servLst[:]
		Q.addrLst=self.addrLst[:]
		for i in range(len(Q.servLst)):
			if Q.servLst[i] in selServ:
				Q.servLst[i]=None
				Q.priceLst[i]=None
				Q.addrLst[i]=None
		Q.addrLst=[x for x in Q.addrLst if x is not None]
		Q.priceLst=[x for x in Q.priceLst if x is not None]
		Q.servLst=[x for x in Q.servLst if x is not None]
		Q._readOnly=True

		return Q

	def to_csv(self,fileName=None):
		if self.priceLst==[]:
			return False

		HEADER=['date','price','service','address']
		if fileName==None:
			fileName='gasbuddyquery_'+self.reqDate.strftime('%Y-%m-%d')+'.csv'
		elif fileName[-4:]!='.csv':
			fileName+='.csv'
		table=self.getTable(rowformat=True,useDate=True)
		pd = pandas.DataFrame(table)
		if os.path.exists(fileName):
			pd.to_csv(fileName, mode='a', index=False, header=False)
		else:
			pd.to_csv(fileName, mode='w', index=False, header=HEADER)
		return True
