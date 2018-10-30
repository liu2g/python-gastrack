# Author      : Zuguang Liu
# Date        : 2018-10-29 01:13:39
# Python Ver  : 3.6
# Description : 

lst=['1','2','a']
print(all(x.isdigit() and len(x)==1 for x in lst))