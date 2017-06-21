#coding: utf-8
import os
import re

rxn_class = []
rxn =[]
A = []
n = []
Ea = []
filename = 'chem_annotated.inp'
with open(filename, 'r') as f:
	lines = f.readlines()
	rxn_flag = False
	for eachline in lines:
		if eachline[:16] == '! Reaction index':
			rxn_flag = True
		if rxn_flag:
			if eachline[:19] =='! Template reaction':
				tmp_rxn_class = eachline.strip().split()[-1]
				rxn_class.append(tmp_rxn_class)
			if eachline[0] != '!' and len(eachline) > 1:
				tmp_line = eachline.strip().split()
				if len(tmp_line) == 4:
					rxn.append(tmp_line[0])
					A.append(tmp_line[1])
					n.append(tmp_line[2])
					Ea.append(tmp_line[3])
					rxn_flag = False
				else:
					print eachline

print 'There are total %s reactions in %s' %(len(rxn), filename)
# for i in range(len(rxn)):
# 	print '%-3s%-20s%-60s%20s%20s%20s' %(i+1, rxn_class[i], rxn[i], A[i], n[i], Ea[i])

q1 = raw_input('Do you want to find a reaction base on reaction class? (y/n):  ')
num_of_rxn = []
if q1 == 'y':
	rxn_classset = list(set(rxn_class))
	rxn_classset.sort()
	print '='*60
	print '%-50s%10s' %('Reaction class', 'Num of reaction')
	print '-'*60
	for item in rxn_classset:
		tmp_num = rxn_class.count(item)
		num_of_rxn.append(tmp_num)
		print '%-50s%10s' %(item, tmp_num)
	print '='*60

q2 = raw_input('Which reaction class do you want to find? (Please type some characters): ')
if q2 != 'n':
	for i in range(len(rxn_classset)):
		if q2 in rxn_classset[i]:
			print '%s has %s reactions.' %(rxn_classset[i], num_of_rxn[i])
			index_of_rxn = []
			for index, rc in enumerate(rxn_class):
				if rc == rxn_classset[i]:
					index_of_rxn.append(index)

	if len(index_of_rxn) <= 200:
		print len(index_of_rxn), index_of_rxn
	else:
		print "There are more than 200 reactions in this class, I don't want to print all of them for you!"


q3 = raw_input('Do you want to provide some reactants or products?(seperated by space)  ')
if q3 != 'n':
	su = []
	s = q3.strip().split()
	for eachs in s:
		print eachs
		su.append(eachs.upper())
	for each in range(len(su)):
		for idx in index_of_rxn:
			if su[each] in rxn[idx].upper():
				print '%-10s%-60s%20s%20s%20s' %(idx, rxn[idx], A[idx], n[idx], Ea[idx])

