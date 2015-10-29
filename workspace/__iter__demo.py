#!/usr/bon/env python3
# -*- coding:utf-8 -*-

from fib import Fib
from student import Student

# __iter__
for n in Fib():
	print('n = ',n)

# __getitem__
f = Fib()
print('f[1] = ', f[1])

# slice
print('f[:5] = ',f[1:10])

# attr
s = Student()
age = s.age()
print(age)
# sex = s.sex()
# print(sex)

#call
dy = Student('Dylan')
dy()
