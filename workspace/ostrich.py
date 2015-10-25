#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a Ostrich module extends from Bird'

__author__='Dylan Lang'

from bird import Bird

class Ostrich(Bird):
	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
	def run(self):
		print('Ostrich is running...')

