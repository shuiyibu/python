#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Student(object):

	def __init__(self,name,score):
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

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
print(lisa.get_grade())