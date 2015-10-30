#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle

d = dict(name = 'bob', age = 20, score = 88)
# 'dumps' not 'dump'
#print(pickle.dumps(d)) 

# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

with open('dump.txt','wb') as f:
	pickle.dump(d,f) # 'dump' not 'dumps'

with open('dump.txt','rb') as f:
	d = pickle.load(f)

print(d)
