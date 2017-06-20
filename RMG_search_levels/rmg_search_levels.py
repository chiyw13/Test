# This file is used to identify the number of reactions with averaged rate
# add new comment line
# git track changes of files
import re
import os
import matplotlib.pyplot as plt

pattern_formula = re.compile(r'([CHOcho]+)\s+(\d+)\s*([CHOcho]*)\s*(\d*)\s*([CHOcho]*)\s*(\d*)')
p_rxn_index = re.compile(r"^! Reaction index: Chemkin #(\d+);\s+.*$")
p_rxn_class = re.compile(r"^! Template reaction: (\S+).*$")
cho = ['C', 'H', 'O']

with open('rmg3_therm.dat', 'r') as f:
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
				tmp_ele = pattern_formula.match(elements)
				element = {}
				if tmp_ele:
					ele = tmp_ele.groups()
					for i in [0, 2, 4]:
						if ele[i] != "":
							element[ele[i].upper()] = int(ele[i+1])

				r_keys =list(set(cho)^set(element.keys()))
				if len(r_keys) > 0:
					for r in r_keys:
						element[r] = '0'

				items = element.items()
				items.sort()
				formula = ''
				for key, value in items:
					formula = formula + key + str(value)
				rmg[tmp_name] = formula
				rmg_e[tmp_name] = element


details = []
with open('chem_annotated.inp','r') as f:
	lines = f.readlines()
	rxn_flag = False
	es_flag = False
	ex_flag = False
	for eachline in lines:
		tmp_rxn_index = p_rxn_index.match(eachline)
		if tmp_rxn_index:
			es_flag = False
			ex_flag = False
			both_es_flag = False
			both_ex_flag = False
			one_ex_flag = False
			rxn_flag = True
			details.append({})
			details[-1]["rxn_index"] = int(tmp_rxn_index.group(1))
			details[-1]["rxn_class"] = ""
			details[-1]["forward"] = ""
			details[-1]["reverse"] = ""
			details[-1]["rxn"] = ""
			details[-1]["reacs"] = []
			details[-1]["prods"] = []
			details[-1]["rf"] = []
			details[-1]["pf"] = []
		if len(eachline) <= 1:
			if es_flag:
				if not both_es_flag:
					details[-1]["reverse"] = "none"
			if ex_flag:
				if not (one_ex_flag or both_ex_flag):
					details[-1]["reverse"] = "none"
			rxn_flag = False

		if rxn_flag:
			tmp_rxn_class = p_rxn_class.match(eachline)
			if tmp_rxn_class:
				details[-1]["rxn_class"]=tmp_rxn_class.group(1)
			if "! Estimated using" in eachline:
				es_flag = True
				details[-1]["forward"] = "average"
			if "! Exact match" in eachline:
				ex_flag = True
				details[-1]["forward"] = "exact"
			
			if es_flag and not ex_flag:
				if "! Both directions are estimates" in eachline:
					details[-1]["reverse"] = "average"
					both_es_flag = True
					
			if ex_flag and not es_flag:
				if "! This direction matched" in eachline:
					details[-1]["reverse"] = "average"
					one_ex_flag = True
				if "! Both directions matched" in eachline:
					details[-1]["reverse"] = "exact"
					both_ex_flag = True
			if ("!" not in eachline) and ("=" in eachline)  and ("+M" not in eachline):
				tmp_rxn = eachline.strip().split()[0]
				details[-1]["rxn"] = tmp_rxn
				tmp_reacts = tmp_rxn.split("=")[0]
				tmp_prodcs = tmp_rxn.split("=")[1]
				if "+" in tmp_reacts:
					for reac in tmp_reacts.split("+"):
						details[-1]["reacs"].append(reac)
				else:
					details[-1]["reacs"].append(tmp_reacts)
				if "+" in tmp_prodcs:
					for prod in tmp_prodcs.split("+"):
						details[-1]["prods"].append(prod)
				else:
					details[-1]["prods"].append(tmp_prodcs)
				
				for reactant in details[-1]["reacs"]:
					if reactant in rmg_e.keys():
						details[-1]["rf"].append(rmg_e[reactant])
				for product in details[-1]["prods"]:
					if product in rmg_e.keys():
						details[-1]["pf"].append(rmg_e[product])

# lebel (ex,av) means the forward reaction rate is exact matched and the reverse reaction rate is averaged.
label = ["(ex,ex)", "(ex,av)", "(ex,no)", "(av,av)", "(av,no)"]
ex_ex = []
ex_av = []
ex_no = []
av_av = []
av_no = []
for i in details:
	# print i["rxn_index"], i["rxn_class"],i["forward"], i["reverse"], i["reacs"], i["prods"], i["rf"], i["pf"]
	# if len(i["reacs"]) == 0:
	# 	print i
	if i["rxn_class"] != "":
		if i["forward"] == "exact" and i["reverse"] == "exact":
			ex_ex.append(i)
		elif i["forward"] == "exact" and i["reverse"] == "average":
			ex_av.append(i)
		elif i["forward"] == "exact" and i["reverse"] == "none":
			ex_no.append(i)
		elif i["forward"] == "average" and i["reverse"] == "average":
			av_av.append(i)
		elif i["forward"] == "average" and i["reverse"] == "none":
			av_no.append(i)

num = [len(ex_ex), len(ex_av), len(ex_no), len(av_av), len(av_no)]

plt.figure(figsize = (9,6))
pos = list(range(len(label)))
width = 0.5
plt.bar(pos, num, width, align='center', alpha=0.5, color='c')

for x,y in zip(pos, num):
    plt.text(x, y+0.05, '%d' % y, ha='center', va= 'bottom')

plt.text(0.5, max(num), 
	     "There are total %d reactions.\n%d reactions have exact matched rate.\n%d reactions have averaged rate." %(sum(num), sum(num[:3]), sum(num[3:])), 
	     ha='left', va= 'top')
plt.xticks(pos, label, size = "small")
plt.xlabel('(Source of foward, Source of reverse)')
plt.ylabel('Number of reactions')
plt.show()

##################################
print "------------------------- number of reactions with averaged forward reaction rate for each reactants size(sum of reactants CxHyOz) -------------------------\n"
# Put all of the reactions with averaged forward reation rates into a list av_for
av_for =[]
for i in av_no:
	av_for.append(i)
for i in av_av:
	av_for.append(i)

reac_size = []
for rxn in av_for:
	cnn = 0
	hnn = 0
	onn = 0
	for n in rxn["rf"]:
		cnn = cnn + int(n['C'])
		hnn = hnn + int(n['H'])
		onn = onn + int(n['O'])
	# reac_size.append('C' + str(cnn) + 'H' + str(hnn) + 'O'+ str(onn))
	reac_size.append('C' + str(cnn) + 'O'+ str(onn))

myset = set(reac_size)
dic_size = {}
for tmp_size in myset:
	dic_size[tmp_size] = reac_size.count(tmp_size)

items = dic_size.items()
items.sort()
for k,v in items:
	print "%-20s%10d" %(k, v)
######################################
print "------------------------- number of reactions with averaged forward reaction rate for each reaction class -------------------------\n"
rxn_class = []
for rxn in av_for:
	rxn_class.append(rxn["rxn_class"])

rxn_set = set(rxn_class)
dic_class = {}
for tmp_class in rxn_set:
	dic_class[tmp_class] = rxn_class.count(tmp_class)

rxn_items = dic_class.items()
rxn_items.sort()
for k, v in rxn_items:
	print "%-50s%10d" %(k, v)

