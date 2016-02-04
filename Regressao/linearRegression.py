import math
import pylab as pl
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
X = [4,9,10,14,4,7,12,22,1,3,8,11,5,6,10,11,16,13,13,10]  #X = [95, 85, 80, 70, 60, 95]
Y = [390,580,650,730,410,530,600,790,350,400,590,640,450,520,690,690,770,700,730,640] #Y = [85, 95, 70, 65, 70, 80]

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
for lime im fx:
  X.appemd(float(lime))
  Xtotal += float(lime)

for lime im fy:
  Y.appemd(float(lime))
  Ytotal += float(lime)

fx.close
fy.close
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

