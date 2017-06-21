# coding: utf-8
import os
import re

class Thermal_data():
	def __init__(self,lines):
		self.lines = lines

	def getName(self):
		name = self.lines[0][0:18].split()[0]
		return name

	def getFormula(self):
		elements = self.lines[0][24:40].strip()
		element = {}
		for i in range((len(elements)+1)/5):
			tmp_e = elements[i*5:i*5+5]
			if tmp_e.split()[0].upper() in 'CHONARHENE':
				element[tmp_e.split()[0]] = tmp_e.split()[1]
		items = element.items()
		items.sort()
		tmp_formula = ''
		for key, value in items:
			tmp_formula = tmp_formula+key+value
		return tmp_formula

	def getTemp(self):
		tmp_T = self.lines[0][45:73].split()
		low_T = tmp_T[0]
		high_T = tmp_T[1]
		if len(tmp_T) == 3:
			mid_T = tmp_T[2]
		else:
			mid_T = high_T
		return float(low_T), float(mid_T), float(high_T)

	# def getTemp(self):
	# 	low_T = self.lines[0][45:55].split()[0]
 #        # high_T = self.lines[0][55:65].split()[0]
 #        # mid_T = self.lines[0][65:73].split()[0]
 #        # print 'Hello'
 #        # temp = [float(low_T), float(mid_T), float(high_T)]
 #        return low_T

	def getCoeff(self):
		coeff = []
		for i in range(1,4):
			for j in range(len(self.lines[i])/15):
				coeff.append(float(self.lines[i][j*15:j*15+15].strip()))
		high_coeff = coeff[:7]
		low_coeff = coeff[7:]
		return low_coeff, high_coeff

if __name__ == "__main__":
	print 'call here'
