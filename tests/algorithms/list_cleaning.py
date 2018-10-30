lst1=[1,2,3,1,4,5,2,3]
lst2=[6,7,8,9,10,11,12,13]
for i in range(1,len(lst1)):
	if lst1[i] in lst1[0:i]:
		pass

lst1=[x for x in lst1 if x is not None]
lst2=[x for x in lst2 if x is not None]

print(lst1)
print(lst2)