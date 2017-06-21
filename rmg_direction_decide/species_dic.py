import re
import os

pattern_label = re.compile(r'^([\S]+)\n$')

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

radicals = {1:'molecule', 2:'radical',3: 'diradical',4:'triradical' }

for k, v in multiplicity.items():
	print "%-20s%20s" %(k, radicals[v])