# Author      : Zuguang Liu
# Date        : 2018-10-28 01:08:03
# Python Ver  : 3.6
# Description : A fun that checks type and raise exception

a=['45220','44141']
if not isinstance(a,str or list): 
	print('this pass')
else:
	print('that pass')