#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum, unique

# define a enumaeration 'Month'
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'))

# output the values 
for name, member in Month.__members__.items():
	print(name,' => ', member, ', ', member.value)

@unique
class Weekday(Enum):
	"""a Weekday enumaeration"""
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.Mon)
print(Weekday['Tue'])
print(Weekday(0))
print(Weekday.Tue.value)





