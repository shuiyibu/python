#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
fib(10)