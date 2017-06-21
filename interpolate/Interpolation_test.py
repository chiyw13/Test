#coding: utf-8

import os
import xlrd
import xlwt
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

T_new = np.linspace(500,1100,31)

mypath = os.getcwd()
data = xlrd.open_workbook('test.xlsx')
names = data.sheet_names()
new_data = xlwt.Workbook()
for name in names:
	print name
	table = data.sheet_by_name(name)
	sh = new_data.add_sheet(name)
	T_exp = table.col_values(0)[1:]
	ncols = table.ncols
	sh.write(0,0,'T(K)')
	for t in range(len(T_new)):
		sh.write(t+1, 0, T_new[t])
	for nc in range(1,ncols):
		s_exp= table.col_values(nc)[1:]
		f_exp = interpolate.interp1d(T_exp,s_exp, kind = "cubic")
		s_exp_new = f_exp(T_new)
		# print table.col_values(nc)[0], s_exp_new
		sh.write(0,nc, table.col_values(nc)[0])
		for i in range(len(s_exp_new)):
			if s_exp_new[i] < 1.0e-10:
				sh.write(i+1, nc, 0.0)
			else:
				sh.write(i+1, nc, s_exp_new[i])

new_data.save('test_new.xls')