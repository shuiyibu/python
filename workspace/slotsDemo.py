#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# from Student import *

class Student(object):
	#using tuple to define permitted bindindg property names
	__slot_=('name','age')

#define a sub-class 'GraduateStudent' extends from 'Student'
class GraduateStudent(Student):
	pass

s = Student()
s.name = 'Micheal'
print(s.name)

#'__slot__' doesn't work in sub_class
g = GraduateStudent()
g.score=99
print(g.score)


