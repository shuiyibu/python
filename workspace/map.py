#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

def f(x):
	return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
#Iterator
print(r)
for x in r:
	print(x)
#Iterable
print(list(r))
#convert integer into string
print(list(map(str,[1,2,3,4,5,6,7,8,9])))






