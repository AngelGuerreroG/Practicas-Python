Hist=[]
from matplotlib.pylab import hist, show
perm = []
for valor in range (-5,6):
	perm.append(valor)

	
part = []
from random import choice
part =[choice (perm) for x in range (3)]
cpart = []
for part in range (10):
	crd = [choice (perm) for x in range (2)]
	cpart.append (crd)

	
from math import sqrt
for part in cpart:
	dist= sqrt(sum([x**2 for x in part]))
	print (dist)
	Hist.append(dist)

hist (Hist,10, (0,10))
show()
