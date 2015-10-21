#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

from collections import Iterable
from collections import Iterator

print(isinstance({},Iterable))

print(isinstance(iter([]),Iterator))