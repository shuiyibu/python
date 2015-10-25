#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a Dog module extends from Mammal'

__author__='Dylan Lang'

from mammal import Mammal
from runnable import Runnable

class Dog(Mammal,Runnable):
	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
	def run(self):
		print('Dog is running...')

