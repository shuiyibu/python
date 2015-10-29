#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a fibonacci module'

__author__ = 'Dylan Lang'

class Fib(object):

	def __init__(self):
		self.a, self.b = 0, 1 # initialize two counters a, b

	def __iter__(self):
		return self # the instance itself is a iter, so return itself

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration();
		return self.a

	def __getitem__(self, n):

		# n is a index
		if isinstance(n, int): 
			self.a, self.b = 0, 1
			for x in range(n):
				self.a, self.b = self.b, self.a + self.b
			return self.a

		# n is a slice
		if isinstance(n, slice):
			self.a, self.b = 0, 1
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			L = []
			for x in range(stop):
				if x >= start:
					L.append(self.a)
				self.a, self.b = self.b, self.a + self.b
			return L

			


	
