#!/usr/bin/env pythion3
#_*_coding: utf-8 _*_

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

a=fact(10)
print("a=%d"%a)