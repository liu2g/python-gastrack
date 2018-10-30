# Author      : Zuguang Liu
# Date        : 2018-10-28 23:37:59
# Python Ver  : 3.6
# Description : 

class MyClass(object):
	x=3

	def _x_type_wrong(self):
		a=2
		print('wrong type idiot')

	def __init__(self):
		return
		
	def __setattr__(self, attrName, value):
		if attrName == 'x':
			if isinstance(value,int):
				self.__dict__['x'] = value
			else:
				self._x_type_wrong()
		

m = MyClass()
m.x = '4'
print(m.__dict__)