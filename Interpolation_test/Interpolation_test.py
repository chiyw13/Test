#coding: utf-8

import os
import xlrd
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

kinds = ["nearest","zero","slinear","quadratic","cubic"]
#"nearest","zero"为阶梯插值, slinear 线性插值, "quadratic","cubic" 为2阶、3阶B样条曲线插值  
mypath = os.getcwd()
data = xlrd.open_workbook('test.xlsx')
table = data.sheet_by_name('test')
T_exp = table.col_values(0)[1:]
s_exp = table.col_values(1)[1:]
T_rmg = table.col_values(2)[1:]
s_rmg = table.col_values(3)[1:]
T_nui = table.col_values(4)[1:]
s_nui = table.col_values(5)[1:]

while T_exp[-1] == '':
	T_exp.pop()
while s_exp[-1] == '':
	s_exp.pop()

T_new = np.linspace(500,1100,61)
n = 4
fig1 = plt.figure(1, (20,6), dpi = 80)
ax1 = plt.subplot(131)
ax1.plot(T_exp, s_exp,'ro', label='exp')
f_exp = interpolate.interp1d(T_exp,s_exp, kind=kinds[n])
s_exp_new = f_exp(T_new)
ax1.plot(T_new, s_exp_new, label = str(kinds[n]))
plt.legend(loc = "upper right")

ax2 = plt.subplot(132)
ax2.plot(T_rmg, s_rmg,'ro', label='rmg')
f_rmg = interpolate.interp1d(T_rmg,s_rmg, kind=kinds[n])
s_rmg_new = f_rmg(T_new)
ax2.plot(T_new, s_rmg_new, label = str(kinds[n]))
plt.legend(loc = "upper right")

ax3 = plt.subplot(133)
ax3.plot(T_nui, s_nui,'ro', label='nui')
f_nui = interpolate.interp1d(T_nui,s_nui, kind=kinds[n])
s_nui_new = f_nui(T_new)
ax3.plot(T_new, s_nui_new, label = str(kinds[n]))
plt.legend(loc = "upper right")
plt.subplots_adjust(left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
plt.show()

s_nui_dis = []
s_rmg_dis = []
s_nui_dis_tot = 0
s_rmg_dis_tot = 0
for i in range(len(T_new)):
	s_nui_dis.append(abs(s_nui_new[i]-s_exp_new[i]))
	s_rmg_dis.append(abs(s_rmg_new[i]-s_exp_new[i]))
	s_nui_dis_tot += s_nui_dis[-1]**2
	s_rmg_dis_tot += s_rmg_dis[-1]**2

plt.figure(2)
plt.plot(T_new, s_nui_dis, label = 'nui-exp')
plt.plot(T_new, s_rmg_dis, label = 'rmg-exp')
plt.legend(loc = 'upper right')
print 'nui-exp = %10.4e, rmg-exp = %10.5e'%(math.sqrt(s_nui_dis_tot/len(T_new)), math.sqrt(s_rmg_dis_tot/len(T_new)))
plt.show()