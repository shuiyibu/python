#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

lists=[1,2,3,4,5,6,7,8,9]
def is_odd(n):
	return n%2==1

print(list(filter(is_odd,lists)))
test_str=['A','','B',None,'C','']

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,test_str)))

#**********generate prime*************

lists=range(1,20)

#define a selection function
def _not_division(n):
	return lambda x:x%n>0

#generate odd lists
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

def primes():
	yield 2 
	it=_odd_iter() #init lists
	while  True:
		n=next(it) # get the first object of lists
		yield n
		it=filter(_not_division(n),it) #construct new lists

#test function
#print all the primes in 1,000
for n in primes():
	if n<1000:
		print(n)
	else:
		break


