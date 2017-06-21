# coding: utf-8
import os
import re
import xlwt
import matplotlib.pyplot as plt
import numpy as np

mypath = os.getcwd()
files = os.listdir(mypath)

file = xlwt.Workbook()
sh = file.add_sheet('species')


# thermfiles = []
# chemfiles = []
# for eachfile in files:
# 	if eachfile[-4:] == '.dat' or eachfile[-4:] == '.DAT':
# 		thermfiles.append(eachfile)
# 	if eachfile[-4:] == '.inp' or eachfile[-4:] == '.INP':
# 		chemfiles.append(eachfile)
cho = ['C', 'H', 'O']
with open('heptane_NUI_therm.dat', 'r') as f:
	nui = {}
	lines = f.readlines()
	for i in range(len(lines)-3):
		line1 = lines[i]
		line2 = lines[i+1]
		line3 = lines[i+2]
		line4 = lines[i+3]
		if len(line1)>=80 and len(line2)>=80 and len(line3)>=80 and len(line4)>=80:
			if line1[79]=='1' and line2[79]=='2' and line3[79]=='3' and line4[79]=='4':
				tmp_name = line1[:18].split()[0]
				elements = line1[24:40].strip()
				element = {}
				for i in range((len(elements)+1)/5):
					tmp_e = elements[i*5:i*5+5]
					if tmp_e.split()[0].upper() in 'CHO':
						element[tmp_e.split()[0].upper()] = tmp_e.split()[1]
				r_keys =list(set(cho)^set(element.keys()))
				if len(r_keys) > 0:
					for r in r_keys:
						if r.upper() != 'HE' and r.upper() != 'NE' and r.upper() != 'AR' and r.upper() != 'N':
							element[r] = '0'

				items = element.items()
				items.sort()
				formula = ''
				for key, value in items:
					formula = formula + key + value
				nui[tmp_name] = formula

with open('rmg1_therm.dat', 'r') as f:
	rmg = {}
	lines = f.readlines()
	for i in range(len(lines)-3):
		line1 = lines[i]
		line2 = lines[i+1]
		line3 = lines[i+2]
		line4 = lines[i+3]
		if len(line1)>=80 and len(line2)>=80 and len(line3)>=80 and len(line4)>=80:
			if line1[79]=='1' and line2[79]=='2' and line3[79]=='3' and line4[79]=='4':
				tmp_name = line1[:18].split()[0]
				elements = line1[24:40].strip()
				element = {}
				for i in range((len(elements)+1)/5):
					tmp_e = elements[i*5:i*5+5]
					if tmp_e.split()[0].upper() in 'CHO':
						element[tmp_e.split()[0].upper()] = tmp_e.split()[1]
				r_keys =list(set(cho)^set(element.keys()))
				if len(r_keys) > 0:
					for r in r_keys:
						if r.upper() != 'HE' and r.upper() != 'NE' and r.upper() != 'AR' and r.upper() != 'N':
							element[r] = '0'

				items = element.items()
				items.sort()
				formula = ''
				for key, value in items:
					formula = formula + key + value
				rmg[tmp_name] = formula

rmg_items = rmg.items()
rmg_items.sort()

nr = 0
for kr, vr in rmg_items:
	sh.write(nr,0,kr)
	sh.write(nr,1,vr)
	same_key = []
	for kn, vn in nui.items():
		if vn == vr:
			same_key.append(kn)
	if len(same_key)>0:
		for i in range(len(same_key)):
			sh.write(nr,i+2,same_key[i])
	nr += 1

file.save('species.xls')

