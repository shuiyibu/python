#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# declare a path variable and the path is the current path
path = 'test.txt'

# write sonmething into 'test.txt'
with open(path,'a') as f:
	f.write('hello biatch')

# read the content of file and output it 
# replacing the 'try...finally' with 'with' allows the code style more simple
with open(path,'r') as f:
	print(f.read())



# read binary file
binarypath='../images/portrait.jpg'
# the type of read is 'rb'
with open(binarypath,'rb') as f:
	print(f.readline()) # the output bytes by hexdecimal
