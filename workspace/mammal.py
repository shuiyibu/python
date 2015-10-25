#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a Mammal module extends from Animal'

__author__='Dylan Lang'

from animal import Animal

class Mammal(Animal):
	# """docstring for Mammal"""
	# def __init__(self, arg):
	# 	super(Mammal, self).__init__()
	# 	self.arg = arg
	def run(self):
		print('Mammal is running...')

mam = Mammal()
# print()
mam.run()
