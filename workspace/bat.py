#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a Bat module extends from Mammal'

__author__='Dylan Lang'

from mammal import Mammal
from flyable import Flyable

class Bat(Mammal,Flyable):
	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
	def run(self):
		print('Bat is running...')

bat=Bat()
bat.fly()

