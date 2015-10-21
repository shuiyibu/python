#/usr/bin/env python 3
#_*_ coding:utf-8 _*_

f=abs
print("f is ",f)
print("f(-10)=",f(-10))
def add(x,y,f):
	return f(x)+f(y)

print("add(-5,-6,f)=",add(-5,-6,f))