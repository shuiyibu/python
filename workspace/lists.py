#!/usr/bin/env python 3
#_*_ coding:utf-8 _*_
import os
L=[x*x for x in range(1,11) if x%2==0]
print(L)

L2=[m+n for m in 'abc' for n in 'xyz']
print(L2)

show_dir=[d for d in os.listdir('.')]
#print(show_dir)
d={'Micheal':95,'Bob':85,'Tracy':60,'Bob':80}
L3=[k+'='+str(v) for k,v in d.items()]
print(L3)

L = ['Hello', 'World', 'IBM', 'Apple']
L= [s.lower() for s in L]
print(L)