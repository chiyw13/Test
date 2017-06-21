# -*- coding: utf-8 -*-
import re
import os

pattern_label = re.compile(r'^([\S]+)\n$')

line_nums = []
label = []
with open('species_dictionary.txt', 'rU') as f:
    lines = f.readlines()
    line_num = 0
    for eachline in lines:
        species = pattern_label.match(eachline)
        if species:
            label.append(species.group(1))
            line_nums.append(line_num)
        line_num = line_num + 1

species_num = 1
for eachspecies in line_nums:
    print 'species num = ',species_num, eachspecies, lines[eachspecies]
    species_num += 1

structures = []
for i, value in enumerate(line_nums):
    if i < len(line_nums)-1:
        # print 'i=', i, 'value=', value
        if 'multiplicity' in lines[value+1]:
            structures.append(lines[value+2:line_nums[i+1]-1])
        else:
            structures.append(lines[value+1:line_nums[i+1]-1])
    else:
        # print 'i=', i, 'value=', value
        if 'multiplicity' in lines[value+1]:
            structures.append(lines[value+2:])
        else:
            structures.append(lines[value+3:])


# line_nums = []
# with open('dictionary.txt', 'rU') as f:
#     lines = f.readlines()
#     line_num = 0
#     for eachline in lines:
#         if not eachline.split():
#             line_nums.append(line_num)
#         line_num = line_num + 1

# print len(lines)

# label = []
# structures = []
# for i, value in enumerate(line_nums):
#     if i == 0:
#         print 'i=', i, 'value=', value
#         label.append(lines[0])
#         label.append(lines[value+1])
#         if 'multiplicity' in lines[1]:
#             structures.append(lines[2:value])
#         else:
#             structures.append(lines[1:value])
#         if 'multiplicity' in lines[value+2]:
#             structures.append(lines[value+3:line_nums[i+1]])
#         else:
#             structures.append(lines[value+2:line_nums[i+1]])
#     elif i > 0 and i < len(line_nums)-1:
#         print 'i=', i, 'value=', value
#         label.append(lines[value+1])
#         if 'multiplicity' in lines[value+2]:
#             structures.append(lines[value+3:line_nums[i+1]])
#         else:
#             structures.append(lines[value+2:line_nums[i+1]])
#     else:
#         if len(lines)-line_nums[-1]<4:
#             exit
#         else:
#             print 'i=', i, 'value=', value
#             label.append(lines[value+1])
#             if 'multiplicity' in lines[value+2]:
#                 structures.append(lines[value+3:])
#             else:
#                 structures.append(lines[value+2:])

with open('input_species.py', 'w+') as f:
    for i, eachlabel in enumerate(label):
        f.write('''
species(
    label=\'''')
        f.write(eachlabel.strip())
        f.write('''\',
    reactive=True,
    structure=adjacencyList(
        \"\"\"\n''')
        for index, value in enumerate(structures[i]):
            f.write('        ')
            if index != len(structures[i])-1:
                f.write(value)
            else:
                f.write(value.strip())
        f.write('''
        \"\"\"),
)
            ''')

# for i, eachlabel in enumerate(label):
#     print '**************'+str(i)+' '+eachlabel+' start**************'
#     for j in structures[i]:
#         print j,
#     print '**************'+str(i)+' '+eachlabel+' end**************'

