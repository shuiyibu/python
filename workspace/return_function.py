#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

f=lazy_sum(1,3,5,7,9)
#output f---the address of memory 
print(f)
#output  the sum of function
print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print("f1==f2:",f1==f2)

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1=count()
# print(f1())

# for x in f1():
# 	print(x)

#print(f1())

def count():
	fs=[]#the value of the list are the name of function f(),rather than the return values
	for i in range(1,4):
		def f():  # not call instantly until the invoke the function f()
			return i*i
		fs.append(f) #the args is the name of function f()
	return fs
f1,f2,f3=count()
print(f1())
