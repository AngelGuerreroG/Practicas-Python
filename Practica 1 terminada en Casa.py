Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Hist=[]
>>> from matplotlib.pylab import hist, show
>>> perm = []
>>> for valor in range (-5,6):
	perm.append(valor)

	
>>> part = []
>>> from random import choice
>>> part =[choice (perm) for x in range (3)]
>>> cpart = []
>>> for part in range (10):
	crd = [choice (perm) for x in range (2)]
	cpart.append (crd)

	
>>> from math import sqrt
>>> for part in cpart:
	dist= sqrt(sum([x**2 for x in part]))
	print (dist)
	Hist.append(dist)

	
5.830951894845301
5.0
4.123105625617661
6.4031242374328485
1.4142135623730951
3.605551275463989
7.0710678118654755
5.0
5.830951894845301
5.0
>>> hist (Hist,10, (0,10))
(array([ 0.,  1.,  0.,  1.,  1.,  5.,  1.,  1.,  0.,  0.]), array([  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.]), <a list of 10 Patch objects>)
>>> show()
>>> 
