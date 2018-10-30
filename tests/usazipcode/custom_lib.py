# Author      : Zuguang Liu
# Date        : 2018-10-28 01:08:03
# Python Ver  : 3.6
# Description : Custom functions that make life easier

def check_type(var,type_to_check,msg):
	if not isinstance(type_to_check,type):
		raise TypeError('The type_to_check argument must be a type')

	if not isinstance(msg,str):
		raise TypeError('The type error message must be a string')

	if not isinstance(var,type_to_check):
		raise TypeError(msg)

	return True

def list_transpose(lst):
	check_type(lst,list,'Input must be a list')
	for x in lst:
		check_type(x,list,'An element of the input must be a list')
		if len(x)!= len(lst[0]):
			raise ValueError('Length of each element must be the same')

	return [list(i) for i in zip(*lst)]