import re

pattern = re.compile(r'^(\S*)\+(\S*)<=>(\S*)\+(\S*).*')
pattern_label = re.compile(r'^([\S]+)\n$')
pattern_formula = re.compile(r'([CHOcho]+)\s+(\d+)\s*([CHOcho]*)\s*(\d*)\s*([CHOcho]*)\s*(\d*)')
cho = ['C', 'H', 'O']

with open('heptane_NUI_therm.dat', 'r') as f:
	nui = {}
	nui_e = {}
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
							element[ele[i].upper()] = ele[i+1]
				else:
					print elements
				r_keys =list(set(cho)^set(element.keys()))
				if len(r_keys) > 0:
					for r in r_keys:
						element[r] = '0'

				items = element.items()
				items.sort()
				formula = ''
				for key, value in items:
					formula = formula + key + value
				nui[tmp_name] = formula
				nui_e[tmp_name] = element

with open("heptane_NUI_chem.inp", 'r') as f:
	lines = f.readlines()
	wlines = []
	for eachline in lines:
		if eachline[0] != '!' and "+M" not in eachline:
			species = pattern.match(eachline)
			if species:
				# print species.groups()
				r1 = species.group(1)
				r2 = species.group(2)
				p1 = species.group(3)
				p2 = species.group(4)
				# print nui_e[r1], nui_e[r2],nui_e[p1], nui_e[p2]
				if r1 in nui_e.keys() and r2 in nui_e.keys() and p1 in nui_e.keys() and p2 in nui_e.keys():
					r1h = int(nui_e[r1]['H'])
					r2h = int(nui_e[r2]['H'])
					p1h = int(nui_e[p1]['H'])
					p2h = int(nui_e[p2]['H'])
					if abs(abs(r1h-r2h)-abs(p1h-p2h)) == 2 or (abs(r1h-r2h) == 1 and abs(p1h-p2h) == 1):
						wline = "%-30s%-30s%-30s%-30s%-10s%-10s%-10s%-10s H %5d H_rev %5d\n" %(r1, r2, p1, p2, nui[r1], nui[r2], nui[p1], nui[p2], abs(r1h-r2h), abs(p1h-p2h))
						wlines.append(wline)

with open('output_nui.txt', 'w+') as fw:
	for line in wlines:
		fw.write(line)
