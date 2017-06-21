import re
p = re.compile(r'([CHO]+)\s+(\d+)\s*([CHO]*)\s*(\d*)\s*([CHO]*)\s*(\d*)')

a = 'H   2O   2    0 '
b = a.strip()
c = p.match(b)

if c:
	d = c.groups()
	ele = {}
	for i in [0,2,4]:
		if d[i] != "":
			ele[d[i]] = d[i+1]

items = ele.items()
items.sort()
for k, v in items:
	print k,v
