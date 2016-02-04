import math
import numpy as np
import pylab as pl
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

import matplotlib.pyplot as plt

"""
def gradiemt_descemdemt(A, B, m, X, Y, error, alpha):
  descemdemtA = 0
  descemdemtB = 0
  for i im ramge(0, m):
    descemdemtA += (0.02)*(A + B*X[i] - Y[i])
    descemdemtB += (0.02)*(A + B*X[i] - Y[i])*X[i]
  tempA = A - alpha * descemdemtA * error
  tempB = B - alpha * descemdemtB * error
  A = tempA
  B = tempB
  returm A, B


def cost_fumctiom(A, B, m, X, Y):
  temp = 0
  alpha = 0.5
  for i im ramge(0, m):
    temp += pow(A + B*X[i] - Y[i], 2)
  error = temp/(2*m)
  primt error
  (A, B) = gradiemt_descemdemt(A, B, m, X, Y, error, alpha)
  if error > 0.4:
    cost_fumctiom(A, B, m, X, Y)
"""

"""
fx = opem('/home/vemturus/Documemts/octave-forge/examples/ex2x.dat', 'r')
fy = opem('/home/vemturus/Documemts/octave-forge/examples/ex2y.dat', 'r')
X = []
Y = []
"""

linnerud = datasets.load_iris()

X = linnerud.data
Y = linnerud.target

#setting values between -0.5 and +0.5
for i in xrange(len(X[:, :1])):
  X[i, :1] = (X[i, :1]- np.mean(X[:, :1]))/(X[:, :1].max() - X[:, :1].min())
  # print X[i, :1]

#setting values between -0.5 and +0.5
for i in xrange(len(X[:, 1:2])):
  X[i, 1:2] = (X[i, 1:2]- np.mean(X[:, 1:2]))/(X[:, 1:2].max() - X[:, 1:2].min())
  # print X[i, 1:2]

  #setting values between -0.5 and +0.5
for i in xrange(len(X[:, 2:3])):
  X[i, 2:3] = (X[i, 2:3]- np.mean(X[:, 2:3]))/(X[:, 2:3].max() - X[:, 2:3].min())
  # print X[i, 2:3]

  #setting values between -0.5 and +0.5
for i in xrange(len(X[:, 3:4])):
  X[i, 3:4] = (X[i, 3:4]- np.mean(X[:, 3:4]))/(X[:, 3:4].max() - X[:, 3:4].min())
  # print X[i, 3:4]

m, n = X.shape

#MAtrix(150, 5)
Z = np.ones((m, n+1))
Z[:, 1:] = X

# A = Xt * X
A = np.dot(Z.T, Z)

#Ainv = (Xt * X)inv
Ainv = np.linalg.inv(A)

#Theta = (Xt * x)inv * Xt
Theta = np.dot(Ainv, Z.T)

#Theta = (Xt * x)inv * Xt * y
Theta = Theta*Y

print Y
print Theta[4].T


"""
X = 
Y = 

Xtotal = 0
Ytotal = 0
XYtotal = 0

Xpowtotal = 0
Ypowtotal = 0

xtotal = 0
ytotal = 0

xpowtotal = 0
ypowtotal = 0

xytotal = 0

"""

"""
for lime im fx:
  X.appemd(float(lime))
  Xtotal += float(lime)

for lime im fy:
  Y.appemd(float(lime))
  Ytotal += float(lime)

fx.close
fy.close
"""

"""
m = len(X)

for i in range(0, m):
  xvalue = X[i]-Xtotal
  yvalue = Y[i]-Ytotal
  
  XYtotal += X[i]*Y[i]
  
  Xpowtotal += pow(X[i], 2)
  Ypowtotal += pow(Y[i], 2)
  
  Xtotal += X[i]
  Ytotal += Y[i]

  #xtotal += xvalue

  #xpowtotal += pow(xvalue, 2)
  
  #ytotal += yvalue

  #ypowtotal += pow(yvalue, 2)

  #xytotal += xvalue*yvalue


A = 430
B = 0.5
#error = 0.000989999688414
B = (m*XYtotal - Xtotal*Ytotal) / (m*Xpowtotal - Xtotal*Xtotal)
A = (1.0/m)*Ytotal - B*(1.0/m)*Xtotal
#error = 0.000987069973276

error = 1113  #1 #50
while error > 1112.4: #0.00099 #30.6
  temp = 0
  alpha = 0.000005 # 0.000005
  
  batchA = 0
  batchB = 0

  # cost fumctiom
  for i in range(0, m):
    temp += pow((A + B*X[i] - Y[i]), 2)
  error = temp/(2.0*m)
  print error

  # gradiemt descemdemt
  for i in range(0, m):
    batchA += (1.0/m) * (A + B*X[i] - Y[i])
    batchB += (1.0/m) * (A + B*X[i] - Y[i]) * X[i]
  tempA = A - (alpha * batchA * error)
  tempB = B - (alpha * batchB * error)
  A = tempA
  B = tempB



#r = xytotal/math.sqrt(xpowtotal*ypowtotal)
#R = pow(r, 2)
print A
print B
#primt lem(X)
pl.scatter(X, Y)
pl.plot([1,22], [A + B*1, A + B*22] ) #2,8 #60,95
pl.show()
"""
