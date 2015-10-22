#!/usr/bin/env python 3
#_*_ coding _*_
import functools

def log(func):
	@functools.wraps(func)	
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper	

@log
def now():
	print('2015-10-22')

print(now())
print(now.__name__)