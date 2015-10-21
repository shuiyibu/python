#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_

lists1=sorted([36, 5, -12, 9, -21])
print(lists1)

lists2=sorted([36, 5, -12, 9, -21], key=abs)
print(lists2)

lists3=sorted(['bob', 'about', 'Zoo', 'Credit'])
print(lists3)

list4=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(list4)

lists5=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(list5)


