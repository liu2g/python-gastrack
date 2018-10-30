# Author      : Zuguang Liu
# Date        : 2018-10-28 04:11:49
# Python Ver  : 3.6
# Description : include a function that transpose a list

def list_transpose(lst):
	return [list(i) for i in zip(*lst)]

alist=[[1,2,3],['a','b']]
print(list_transpose(alist))