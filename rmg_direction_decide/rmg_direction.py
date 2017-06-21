import re

pattern = re.compile(r'^(\S*)\+(\S*)=(\S*)\+(\S*).*')
pattern_label = re.compile(r'^([\S]+)\n$')
cho = ['C', 'H', 'O']

with open('species_dictionary.txt', 'r') as f:
    lines = f.readlines()
    multiplicity = {}
    for line_num, eachline in enumerate(lines):
        species = pattern_label.match(eachline)
        if species:
        	if "multiplicity" in lines[line_num+1]:
        		multiplicity[species.group(1)] = int(lines[line_num+1].strip().split()[-1])
        	else:
        		multiplicity[species.group(1)] = 1

with open('therm.dat', 'r') as f:
	rmg = {}
	rmg_e = {}
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
						element[r] = '0'

				items = element.items()
				items.sort()
				formula = ''
				for key, value in items:
					formula = formula + key + value
				rmg[tmp_name] = formula
				rmg_e[tmp_name] = element

with open("chem_annotated.inp", 'r') as f:
	lines = f.readlines()
	rxn_flag = False
	rxnclass = []
	con0=[]
	con1=[]
	con2=[]
	con3=[]
	con4=[]
	con5=[]
	wlines = []
	for eachline in lines:
		if "! Template reaction: H_Abstraction" in eachline:
			rxn_flag = True
		if rxn_flag and "This direction matched an entry" in eachline:
			es_for = "exact"
			es_rev = "average"
		if rxn_flag and "Both directions are estimates" in eachline:
			es_for = "average"
			es_rev = "average"
		if rxn_flag and "Both directions matched explicit" in eachline:
			es_for = "exact"
			es_rev = "exact"

		if rxn_flag and "!" not in eachline:
			species = pattern.match(eachline)
			if species:
				r1 = species.group(1)
				r2 = species.group(2)
				p1 = species.group(3)
				p2 = species.group(4)
				r1c = int(rmg_e[r1]['C'])
				r1h = int(rmg_e[r1]['H'])
				r1o = int(rmg_e[r1]['C'])
				r2c = int(rmg_e[r2]['C'])
				r2h = int(rmg_e[r2]['H'])
				r2o = int(rmg_e[r2]['O'])
				p1c = int(rmg_e[p1]['C'])
				p1h = int(rmg_e[p1]['H'])
				p1o = int(rmg_e[p1]['O'])
				p2c = int(rmg_e[p2]['C'])
				p2h = int(rmg_e[p2]['H'])
				p2o = int(rmg_e[p2]['O'])

				# wline = ""
				# for i in range(1,5):
				# 	for ele, num in rmg_e[species.group(i)].items():
				# 		tmp_wline = "%5s%5s" %(ele, num)
				# 		wline = wline + tmp_wline
				# 	wline = wline + "%5d" %(multiplicity[species.group(i)])
				# wline = wline + '%20s%20s\n' %(es_for, es_rev)
				wline = "%-20s%-20s%-20s%-20s  H  %5d  H_rev  %5d%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], abs(r1h-r2h), abs(p1h-p2h), es_for, es_rev)
				wlines.append(wline)

				# if r1c == p1c and r1o == p1o and abs(r1h-p1h)==1:
				# 	if r1h > p1h:
				# 		if r1c >= r2c:
				# 			if r1h > r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], r1c-r2c, r1h-r2h, p2h-p1h, r1o-r2o, es_for, es_rev, "Hlarge") 
				# 				con0.append(wline)
				# 			elif r1h == r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], r1c-r2c, r1h-r2h, p2h-p1h, r1o-r2o, es_for, es_rev, "Hequal")
				# 				con1.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], r1c-r2c, r1h-r2h, p2h-p1h, r1o-r2o, es_for, es_rev, "Hsmall")
				# 				con2.append(wline)
				# 		else:
				# 			if r1h > r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], r1c-r2c, r1h-r2h, p2h-p1h, r1o-r2o, es_for, es_rev, "Csmall")
				# 				con3.append(wline)
				# 			elif r1h == r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], r1c-r2c, r1h-r2h, p2h-p1h, r1o-r2o, es_for, es_rev, "Csmall,Hequal")
				# 				con4.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p1], rmg[p2], r1c-r2c, r1h-r2h, p2h-p1h, r1o-r2o, es_for, es_rev, "Csmall,Hsmall")
				# 				con5.append(wline)
				# 	else:
				# 		if r2c >= r1c:
				# 			if r2h > r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p2], rmg[p1], r2c-r1c, r2h-r1h, p1h-p2h, r2o-r1o, es_for, es_rev, "Hlarge")
				# 				con0.append(wline)
				# 			elif r2h == r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p2], rmg[p1], r2c-r1c, r2h-r1h, p1h-p2h, r2o-r1o, es_for, es_rev, "Hequal")
				# 				con1.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p2], rmg[p1], r2c-r1c, r2h-r1h, p1h-p2h, r2o-r1o, es_for, es_rev, "Hsmall")
				# 				con2.append(wline)
				# 		else:
				# 			if r2h > r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p2], rmg[p1], r2c-r1c, r2h-r1h, p1h-p2h, r2o-r1o, es_for, es_rev, "Csmall")
				# 				con3.append(wline)
				# 			elif r2h == r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p2], rmg[p1], r2c-r1c, r2h-r1h, p1h-p2h, r2o-r1o, es_for, es_rev, "Csmall,Hequal")
				# 				con4.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p2], rmg[p1], r2c-r1c, r2h-r1h, p1h-p2h, r2o-r1o, es_for, es_rev, "Csmall,Hsmall")
				# 				con5.append(wline)

				# else:
				# 	if r1h > p2h:
				# 		if r1c >= r2c:
				# 			if r1h > r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p2], rmg[p1], r1c-r2c, r1h-r2h, p1h-p2h, r1o-r2o, es_for, es_rev, "Hlarge")
				# 				con0.append(wline)
				# 			elif r1h == r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p2], rmg[p1], r1c-r2c, r1h-r2h, p1h-p2h, r1o-r2o, es_for, es_rev, "Hequal")
				# 				con1.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p2], rmg[p1], r1c-r2c, r1h-r2h, p1h-p2h, r1o-r2o, es_for, es_rev, "Hsmall")
				# 				con2.append(wline)
				# 		else:
				# 			if r1h > r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p2], rmg[p1], r1c-r2c, r1h-r2h, p1h-p2h, r1o-r2o, es_for, es_rev, "Csmall")
				# 				con3.append(wline)
				# 			elif r1h == r2h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p2], rmg[p1], r1c-r2c, r1h-r2h, p1h-p2h, r1o-r2o, es_for, es_rev, "Csmall,Hequal")
				# 				con4.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r1], rmg[r2], rmg[p2], rmg[p1], r1c-r2c, r1h-r2h, p1h-p2h, r1o-r2o, es_for, es_rev, "Csmall,Hsmall")
				# 				con5.append(wline)
				# 	else:
				# 		if r2c >= r1c:
				# 			if r2h > r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p1], rmg[p2], r2c-r1c, r2h-r1h, p2h-p1h, r2o-r1o, es_for, es_rev, "Hlarge")
				# 				con0.append(wline)
				# 			elif r2h == r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p1], rmg[p2], r2c-r1c, r2h-r1h, p2h-p1h, r2o-r1o, es_for, es_rev, "Hequal")
				# 				con1.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p1], rmg[p2], r2c-r1c, r2h-r1h, p2h-p1h, r2o-r1o, es_for, es_rev, "Hsmall")
				# 				con2.append(wline)
				# 		else:
				# 			if r2h > r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p1], rmg[p2], r2c-r1c, r2h-r1h, p2h-p1h, r2o-r1o, es_for, es_rev, "Csmall")
				# 				con3.append(wline)
				# 			elif r2h == r1h:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p1], rmg[p2], r2c-r1c, r2h-r1h, p2h-p1h, r2o-r1o, es_for, es_rev, "Csmall,Hequal")
				# 				con4.append(wline)
				# 			else:
				# 				wline = "%-20s%-20s%-20s%-20sC  %5d  H  %5d  H_rev  %5d  O  %5d%20s%20s%20s\n" %(rmg[r2], rmg[r1], rmg[p1], rmg[p2], r2c-r1c, r2h-r1h, p2h-p1h, r2o-r1o, es_for, es_rev, "Csmall,Hsmall")
				# 				con5.append(wline)
			rxn_flag = False
			es_for = ""
			es_rev = ""

# print "C large  H large:  ", len(con0)
# print "C large  H equal:  ", len(con1)
# print "C large  H small:  ", len(con2)
# print "C small  H large:  ", len(con3)
# print "C small  H equal:  ", len(con4)
# print "C small  H small:  ", len(con5)

with open('output.txt', 'w+') as fw:
	for line in wlines:
		fw.write(line)
# 	fw.write("------------------------------  C large  H large  ------------------------------\n")
# 	for line in con0:
# 		fw.write(line)
# 	fw.write("------------------------------  C large  H equal  ------------------------------\n")
# 	for line in con1:
# 		fw.write(line)
# 	fw.write("------------------------------  C large  H small  ------------------------------\n")
# 	for line in con2:
# 		fw.write(line)
# 	fw.write("------------------------------  C small  H large  ------------------------------\n")
# 	for line in con3:
# 		fw.write(line)
# 	fw.write("------------------------------  C small  H equal  ------------------------------\n")
# 	for line in con4:
# 		fw.write(line)
# 	fw.write("------------------------------  C small  H small  ------------------------------\n")
# 	for line in con5:
# 		fw.write(line)