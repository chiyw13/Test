#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

a = range(1,10)
x = range(20,30)
b = []
c = []
y = []
z = []
for i in a:
	b.append(i**2)
	c.append(i*10)
for i in x:
	y.append(i*2-5)
	z.append(i*5-10)

plt.figure(1, figsize = (20,10), dpi = 60)
ax1 = plt.subplot(121)
line1, = ax1.plot(a, b, 'r-',linewidth = 2.0, label = 'line1')
line2, = ax1.plot(a, c, 'b-', linewidth = 2.0, label = 'line2')
legend_S = ax1.legend(loc = 'upper left', bbox_to_anchor = (0.1, 0.8), fontsize = 18)
legend_S.get_frame().set_edgecolor('None')
plt.xlabel('Temperature (K)', fontsize = 18)
plt.ylabel('H, S, Cp (kcal/mol/K)', fontsize = 18)
plt.title('Title', fontsize = 24)
plt.xlim(0,10)
plt.xticks(np.linspace(0,10,21))
plt.ylim(0,100)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

ax2 = plt.subplot(122)
print_str = '''
This is just a test.
line1
line2
line3
line4
'''
plt.xlim(0, 1)
plt.ylim(0, 1)
ax2.set_xticks([])
ax2.set_yticks([])
plt.text(0.5, 0.5,print_str, horizontalalignment = 'left', fontsize = 18)
plt.show()



# plt.figure(1) # 创建图表1
# plt.figure(2) # 创建图表2
# ax1 = plt.subplot(211) # 在图表2中创建子图1
# ax2 = plt.subplot(212) # 在图表2中创建子图2
 
# x = np.linspace(0, 3, 100)
# for i in xrange(5):
#     plt.figure(1)  #❶ # 选择图表1
#     plt.plot(x, np.exp(i*x/3))
#     plt.sca(ax1)   #❷ # 选择图表2的子图1
#     plt.plot(x, np.sin(i*x))
#     plt.sca(ax2)  # 选择图表2的子图2
#     plt.plot(x, np.cos(i*x))
 
# plt.show()