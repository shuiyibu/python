#!/usr/bin/env python 3
#_*_ coding _*_
import functools



def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper

@log #after the function log defined
def now():
	print('2015-10-21')

f=now
print('f:',f)
print('f():',f())# the output is null
print('now.__name__:',now.__name__)#two underlines
print('----------decorator---------------')
print(now())