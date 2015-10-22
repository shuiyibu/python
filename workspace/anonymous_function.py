#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

f=lambda x:x*x
print(f)

#set the anonymous function as returned value 
def build(x,y):
	return lambda: x*x+y*y

f=build(3,4)	
print(f)
print(f())