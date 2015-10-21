#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

dict_stuff={'Micheal':95,'Bob':85,'Tracy':60}

#output key
for key in dict_stuff:
	print(key)
#output values
for values in dict_stuff.values():
	print(values)
#output k-v
for k,v in dict_stuff.items():
	print("k=%s,v=%s"%(k,v))

from collections import Iterable
print("isinstance('abc',Iterable):",isinstance('abc',Iterable))
for i,value in enumerate(['a','b','c']):
	print(i,value)
