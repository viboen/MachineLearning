import math
import numpy as np
import pylab as pl
import os, sys
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

#X = open()
filenameX = "datax.dat"
filenameY = "datay.dat"

#inicialize X and Y arrays
X, Y = [], []
#inicialize pow of elements
XYtotal = 0
Xpowtotal = 0
Ypowtotal = 0

#read files
if os.path.exists(filenameX):
	fx = open(filenameX, 'r')

if os.path.exists(filenameY):
	fy = open(filenameY, 'r')

#create a list of floats from the files
for line in fx:
	X.extend([float(i) for i in line.split()])
for line in fy:
	Y.extend([float(i) for i in line.split()])

# 
for i in xrange(len(X)):
	XYtotal   +=  X[i] * Y[i]
	Xpowtotal +=  pow(X[i], 2)
	Ypowtotal +=  pow(Y[i], 2)

# Estipulate line equation (hypothesis)
B = (len(X)*XYtotal - sum(X)*sum(Y)) / (len(X)*Xpowtotal - sum(X)*sum(X))
A = (1.0/(len(X)))*sum(Y) - B*(1.0/len(X))*sum(X)

ERROR = 4
while ERROR > 3.5:
	temp = 0
	alpha = 0.001

	# COST FUNCTION
	for i in xrange(len(X)):
		temp += pow((A + B * X[i] - Y[i]), 2)
	ERROR = temp / (2.0*len(X))
	print '{0:.10f}'.format(float(ERROR))

	batchA = 0
	batchB = 0
	# GRADIENT DESCENDENT
	for i in xrange(len(X)):
		batchA += (1.0/len(X) * (A + B * X[i] - Y[i]))
		batchA += (1.0/len(X) * (A + B * X[i] - Y[i]) * X[i])


	tempA = A - (alpha * batchA * ERROR)
  	tempB = B - (alpha * batchB * ERROR)

  	#new linear equation
  	A = tempA
  	B = tempB


#Plot X's and Y's
pl.scatter(X, Y)
pl.plot( [min(X), max(X)], [A+B*min(X), A+B*max(X)] )
pl.show()
