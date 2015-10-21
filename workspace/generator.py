#!usr/bin/env python 3
# _*_ coding:utf-8 _*_

#list
L=[x*x for x in range(10)]
print(L)
#generator
g=(x*x for x in range(10))
print(g)#输出内存地址
#输出g的值
for n in g:
	print(n)
#switch values
a,b,c=1,2,3
a,b,c=c,a,b
print(a,b,c)
a,b,c=1,2,3
#a,b=b,a
a, b = b, a
print(a,b)

#将fib函数变为generator
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b#print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
fib=fib(10)
print(fib)
print('----for-----')
#for无法取得generator的返回值
for x in fib:
	print(x)
print('----while-----')
#while取得generator的返回值
fib=fib(10)
while True:#True首字母必须大写
	try:
		x=next(fib)
		print('fib:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
