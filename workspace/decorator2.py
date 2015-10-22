#!/usr/bin/env python 3
#_*_ coding _*_

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s%s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2015-10-22')

print(now())