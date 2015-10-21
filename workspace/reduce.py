#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_
from functools import reduce

#definded sum function
def add(x,y):
	return x+y
r=reduce(add,[1,2,3,4,5,6,7,8,9])
print(r)
#built-in sum() function
print(sum([1,2,3,4,5,6,7,8,9]))
#convert lists into integer
def fn(x,y):
	return x*10+y
r=reduce(fn,[1,2,3,4,5])
print(r)
#convert String to int
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))	
print(str2int(['1','2','3','4','5','6','7','8','9']))
#simplified str2int(s)
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

