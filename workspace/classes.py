#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Student(object):
	name='Student'

#declare a instance variable 's'	
s = Student()
#print the value of class variable 'name' of Class 'Student'
print(s.name)

#assign values to 's.name'
s.name = 'Micheal'
print ('---assign---',s.name)

#delete the assigned value of 's.name'
del s.name
print('---del---',s.name)
