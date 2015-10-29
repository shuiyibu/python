#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Student(object):
	
	def __init__(self,name='',score=0):
		self.__name=name
		self.__score=score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self,name):
		self.__name=name

	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('Bad Score')

	def print_score(self):
		print('%s:%s'%(self.__name,self.__score))

	def get_grade(self):
		if self.__score>=90:
			return 'A'
		elif self.__score >=60:
			return 'B'
		else:
			return 'C'
    #defined the 'str'
	def __str__(self):
		return 'Student object(name:%s)'%self.__name

	# defined 'getattr'
	def __getattr__(self, attr):
		if attr == 'age':
			return lambda: 25
		# raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
		# raise AttributeError('\'Student\' object has-- no attribute \'%s\'' % attr)

    # define a callable class
	def __call__(self):
		print('My name is %s' % self.__name)


	__repr__ = __str__



