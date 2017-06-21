#coding:utf-8

import re
import os

mypath = os.getcwd()
files = os.listdir(mypath)
with open('test.dat', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)-3):
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        line4 = lines[i+3]
        if len(line1)>=80 and len(line2)>=80 and len(line3)>=80 and len(line4)>=80:
            if line1[79]=='1' and line2[79]=='2' and line3[79]=='3' and line4[79]=='4':
                print '----------------------------------',lines[i].split()[0],'----------------------------------'
                print line1, line2, line3, line4
                name = line1[0:18].split()[0]
                elements = line1[24:40].strip()
                low_T = line1[45:55].split()[0]
                high_T = line1[55:65].split()[0]
                mid_T = line1[65:73].split()[0]
                element = {}
                for e in range((len(elements)+1)/5):
                    tmp_e = elements[e*5:e*5+5]
                    element[tmp_e.split()[0]]=tmp_e.split()[1]
                    
                coff = []
                linelist = [line2[:75], line3[:75], line4[:60]]
                for j in range(3):
                    for k in range(len(linelist[j])/15):
                        coff.append(linelist[j][k*15:15+k*15])
                print name
                print element
                print low_T, mid_T, high_T
                print len(coff), coff
                
                
                        
            
