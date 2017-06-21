# coding: utf-8

import os
import re
import numpy as np
import math
import matplotlib.pyplot as plt

with open('chem_annotated.inp', 'r') as f:
	lines = f.readlines()
	total = len(lines)
	flag = False
	num = []
	i = 0
	for eachline in lines:
		if eachline[0] =='!':
			flag = True
			i = i + 1
		if len(eachline) == 1 and flag and i > 7:
			flag = False
			num.append(i)
			i = 0

print len(num)

dic_n = {}
for n in num:
	dic_n[n] = num.count(n)

items = dic_n.items()
items.sort()

print '='*40
print '%20s%20s' %('num of comment line', 'num of reactions')
print '-'*40
x = 0
for key,value in items:
	print '%20s%20s' %(key, value)
	if key > 15:
		x = x + (key-15)*value

print '='*40
print 'Total %s lines, %s waste lines,  saving %10.2f' %(total, x, x*1.0/total)




