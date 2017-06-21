#coding:utf-8
T = [298.15, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
Ru = 8.314
kcal_to_J = 4184.0
# Units [Ru: J/mol/K]  [H: kcal/mol/K]  [S: kcal/mol]  [Cp: kcal/mol/K] [G: kcal/mol/K]
import math

class Calcthermal:
	def __init__(self, temp, low_c, high_c):
		self.temp = temp
		self.low_c = low_c
		self.high_c = high_c

	def getS(self):
		therm_S = []
		for i, eacht in enumerate(T):
			if eacht <= self.temp[1]:
				tmp_S = Ru*(self.low_c[0]*math.log(eacht)+self.low_c[1]*eacht+self.low_c[2]*(eacht**2)/2.0+self.low_c[3]*(eacht**3)/3.0+self.low_c[4]*(eacht**4)/4.0+self.low_c[6])/kcal_to_J
			else:
				tmp_S = Ru*(self.high_c[0]*math.log(eacht)+self.high_c[1]*eacht+self.high_c[2]*(eacht**2)/2.0+self.high_c[3]*(eacht**3)/3.0+self.high_c[4]*(eacht**4)/4.0+self.high_c[6])/kcal_to_J
			therm_S.append(tmp_S)
		return therm_S

	def getH(self):
		therm_H = []
		for i, eacht in enumerate(T):
			if eacht <= self.temp[1]:
				tmp_H = Ru*(self.low_c[0]*eacht+self.low_c[1]*(eacht**2)/2.0+self.low_c[2]*(eacht**3)/3.0+self.low_c[3]*(eacht**4)/4.0+self.low_c[4]*(eacht**5)/5.0+self.low_c[5])/kcal_to_J
			else:
				tmp_H = Ru*(self.high_c[0]*eacht+self.high_c[1]*(eacht**2)/2.0+self.high_c[2]*(eacht**3)/3.0+self.high_c[3]*(eacht**4)/4.0+self.high_c[4]*(eacht**5)/5.0+self.high_c[5])/kcal_to_J
			therm_H.append(tmp_H)
		return therm_H

	def getCp(self):
		therm_Cp = []
		for i, eacht in enumerate(T):
			if eacht <= self.temp[1]:
				tmp_Cp = Ru*(self.low_c[0]+self.low_c[1]*eacht+self.low_c[2]*(eacht**2)+self.low_c[3]*(eacht**3)+self.low_c[4]*(eacht**4))/kcal_to_J
			else:
				tmp_Cp = Ru*(self.high_c[0]+self.high_c[1]*eacht+self.high_c[2]*(eacht**2)+self.high_c[3]*(eacht**3)+self.high_c[4]*(eacht**4))/kcal_to_J
			therm_Cp.append(tmp_Cp)
		return therm_Cp