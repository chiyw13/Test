#coding: utf-8
# This is the main script, and it will call other scripts
import os
import re
import Extract_thermaldata as td
import Calcthermal as ca
import matplotlib.pyplot as plt
import numpy as np

T = [298.15, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
mypath = os.getcwd()
files = os.listdir(mypath)

thermfiles = []
chemfiles = []
for eachfile in files:
	if eachfile[-4:] == '.dat' or eachfile[-4:] == '.DAT':
		thermfiles.append(eachfile)
	if eachfile[-4:] == '.inp' or eachfile[-4:] == '.INP':
		chemfiles.append(eachfile)

prompt_q = raw_input('Do you want to compare the thermal data for two species? (y/n): ')
while prompt_q == 'y':
	# The element in the input formula should be in "C H O N" order
	input_formula = raw_input('Please enter the formula of species: ').upper()

	# Extract the four lines thermal data for each species into a linelist
	# and find the species that has the same formula as what you want to find
	dic_temp = []
	dic_low_coeff = []
	dic_high_coeff = []
	for eachfile in thermfiles:
		with open(eachfile, 'r') as f:
			print eachfile
			lines = f.readlines()
			dic_temp.append({})
			dic_low_coeff.append({})
			dic_high_coeff.append({})
			for i in range(len(lines)-3):
				line1 = lines[i]
				line2 = lines[i+1]
				line3 = lines[i+2]
				line4 = lines[i+3]
				if len(line1)>=80 and len(line2)>=80 and len(line3)>=80 and len(line4)>=80:
					if line1[79]=='1' and line2[79]=='2' and line3[79]=='3' and line4[79]=='4':
						linelist = [line1[:73], line2[:75], line3[:75], line4[:60]]
						tmp_therm = td.Thermal_data(linelist)
						tmp_name = tmp_therm.getName()
						tmp_name = tmp_name.upper()
						# print tmp_name
						tmp_formula = tmp_therm.getFormula()
						tmp_temp = tmp_therm.getTemp()
						tmp_low_coeff, tmp_high_coeff = tmp_therm.getCoeff()
						dic_temp[-1][tmp_name] = tmp_temp
						dic_low_coeff[-1][tmp_name] = tmp_low_coeff
						dic_high_coeff[-1][tmp_name] = tmp_high_coeff
						if tmp_formula == input_formula:
							print tmp_name
							# for each in linelist:
							# 	print each
							# print tmp_name,'\n', tmp_temp,'\n', tmp_low_coeff,'\n', tmp_high_coeff

	# Ask user for the exact tw species in two chemkin file that user want to compare
	in_species = []
	for i, eachfile in enumerate(thermfiles):
		enter = True
		str_prompt = "Please enter the species name you want to compare in '"+ eachfile + "':  "
		tmp_species = raw_input(str_prompt).upper()
		while enter == True:
			if tmp_species in dic_temp[i].keys():
				in_species.append(tmp_species)
				enter = False
				break
			else:
				tmp_species = raw_input("The species name is not exist in '"+ eachfile + "', please enter again:  ").upper()

	# Get the S, H, Cp for the two species you want to compare
	species_S = []
	species_H = []
	species_Cp =[]
	for i, s in enumerate(in_species):
		print s
		print dic_temp[i][s]
		print dic_low_coeff[i][s]
		print dic_high_coeff[i][s]
		species_therm = ca.Calcthermal(dic_temp[i][s], dic_low_coeff[i][s], dic_high_coeff[i][s])
		species_S.append(species_therm.getS())
		species_H.append(species_therm.getH())
		species_Cp.append(species_therm.getCp())
		for i, t in enumerate(T):
			if i == 0:
				print "="*61
				print "|%10s|%15s|%15s|%16s|" %("Temp", "Entropy S", "Enthalpy H", "Heat capacity Cp")
				print "-"*61
				print "|%10s|%15s|%15s|%16s|" %("K", "kcal/mol/K", "kcal/mol", "kcal/mol/K")
			print "|%10.2f|%15.3e|%15.3e|%16.3e|" %(t, species_S[-1][i], species_H[-1][i], species_Cp[-1][i])
			if i == len(T)-1:
				print "="*61
		
	# Plot the H, S, Cp plots for two species in one figure and list the difference between 
	# the H, S, Cp between these two species
	output_fig = raw_input('Do you want to seen the figure? (y/n): ')
	if output_fig == 'y':
		plt.figure(1, figsize = (20,10), dpi = 80)

		ax1 = plt.subplot(221)
		ax1.plot(T,species_S[0], 'red', linewidth = 2.0, label = in_species[0])
		ax1.plot(T, species_S[1], 'black', linewidth = 2.0, label = in_species[1])
		legend_S = ax1.legend(loc = 'upper left', bbox_to_anchor = (0.05, 0.95), fontsize = 18)
		legend_S.get_frame().set_edgecolor('None')
		plt.xlabel('Temperature (K)', fontsize = 18)
		plt.ylabel('Entropy S (kcal/mol/K)', fontsize = 18)
		plt.xlim(T[1],T[-1])
		plt.subplots_adjust(left = 0.05, bottom = 0.05, right = 0.95, top = 0.95)

		ax2 = plt.subplot(222)
		ax2.plot(T,species_H[0], 'red', linewidth = 2.0, label = in_species[0])
		ax2.plot(T, species_H[1], 'black', linewidth = 2.0, label = in_species[1])
		legend_S = ax2.legend(loc = 'upper left', bbox_to_anchor = (0.05, 0.95), fontsize = 18)
		legend_S.get_frame().set_edgecolor('None')
		plt.xlabel('Temperature (K)', fontsize = 18)
		plt.ylabel('Enthalpy H (kcal/mol)', fontsize = 18)
		plt.xlim(T[1],T[-1])
		plt.subplots_adjust(left = 0.05, bottom = 0.05, right = 0.95, top = 0.95)

		ax3 = plt.subplot(223)
		ax3.plot(T,species_Cp[0], 'red', linewidth = 2.0, label = in_species[0])
		ax3.plot(T, species_Cp[1], 'black', linewidth = 2.0, label = in_species[1])
		legend_S = ax3.legend(loc = 'upper left', bbox_to_anchor = (0.05, 0.95), fontsize = 18)
		legend_S.get_frame().set_edgecolor('None')
		plt.xlabel('Temperature (K)', fontsize = 18)
		plt.ylabel('Heat capacity (kcal/mol/K)', fontsize = 18)
		plt.xlim(T[1],T[-1])
		plt.subplots_adjust(left = 0.05, bottom = 0.05, right = 0.95, top = 0.95)

		ax4 = plt.subplot(224)
		plt.xlim(0, 1)
		plt.ylim(0, 1)
		ax4.set_xticks([])
		ax4.set_yticks([])
		T_i = T.index(800)
		DeltH = species_H[0][T_i]-species_H[1][T_i]
		DeltS = species_S[0][T_i]-species_S[1][T_i]
		DeltCp = species_Cp[0][T_i]-species_Cp[1][T_i]
		print_str = '''
	T = 800K
	The differences of the H, S, Cp between
	%s  and   %s  are:
	DeltS  = %10.5f  kcal/mol/K
	DeltH  = %10.5f  kcal/mol
	DeltCp = %10.5f  kcal/mol/K''' %(in_species[0], in_species[1], DeltS, DeltH, DeltCp)
		plt.text(0.1, 0.2,print_str, horizontalalignment = 'left', fontsize = 18)
		print print_str

		# In case a blank figure would be saved, you should save the figure before show it
		save_fig = mypath + os.sep + 'Figures' + os.sep + in_species[0] +'_vs_' + in_species[1] +'.jpg'
		plt.savefig(save_fig)
		plt.show()
	prompt_q = raw_input('Do you want to compare the thermal data for other two species? (y/n): ')

