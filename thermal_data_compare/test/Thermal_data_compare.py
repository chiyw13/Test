# coding: utf-8
# This script was used to compare the thermal dynamic data for the same species in two chemkin files
# Two thermal dynamic file name as xxx.dat and yyy.dat should be included in this folder
# To run this script, you may need to enter the two species that need to be compared 
# This script will show you the Cp, S, H plot in one figure

import re
import os
mypath = os.getcwd()
files = os.listdir(mypath)

thermfile = []
chemfile = []
for eachfile in files:
	if eachfile[-4:] == '.dat' or eachfile[-4:] == '.DAT':
		thermfile.append(eachfile)
	if eachfile[-4:] == '.inp' or eachfile[-4:] == '.INP':
		chemfile.append(eachfile)

for t_file in chemfile:
	with open(t_file, 'r') as f:
		species = []
		lines = f.readlines()
		species_flag = False
		for eachline in lines:
			if 'SPECIES' in eachline or 'species' in eachline:
				species_flag = True
			if 'end' in eachline or 'END' in eachline:
				species_flag = False
			if species_flag:
				tmp_species = eachline.split()
				while tmp_species:
					species.append(tmp_species.pop())

		print '----------------------', t_file, '----------------------'

		i = 0
		for eachspecies in species:
			if i < 10:
				print eachspecies,
				i = i + 1
			else:
				i = 0
				print '\n'
