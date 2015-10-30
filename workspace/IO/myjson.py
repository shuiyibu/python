#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

d = dict(name = 'bob', age = 20, score = 88)
json.dumps(d)

# with open('myjson.txt','w') as f:
# 	json.dump(f)