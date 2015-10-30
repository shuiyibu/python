#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO

f = StringIO()
f.write('Hello ')
f.write('Dylan')
print(f.getvalue())

with StringIO('Tomorrow is Hollywood!\n holycraped ') as of:
	while True:
		s = of.readline()
		if s == '':
			break
		print(s.strip())



