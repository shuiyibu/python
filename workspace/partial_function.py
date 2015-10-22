#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_
import functools

#base is the code format of '123456'
a=int('123456',base=8)
#the format of output value is decimalism
print(a)

b=int('123456',base=16)
print(b)

def int2(x,base=2):
	return int(x,base)

c=int2('100010101001')
print(c)

#the functools is more simplified---partial()
int2=functools.partial(int,base=2)
d=int2('10101001101')
print('d:',d)

#change the value of parameter 'base'
e=int2('100001011',base=10)
print('e:',e)