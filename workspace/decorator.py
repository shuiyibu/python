#!/usr/bin/env python 3
#_*_ coding _*_

def now():
	print('2015-10-21')

f=now
f()
print(f())# the output is null
now._name_
print(now._name_)
