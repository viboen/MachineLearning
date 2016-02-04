#!/usr/bin/python

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

import matplotlib.pyplot as plt

iris = datasets.load_iris()

X_iris = iris.data
y_iris = iris.target

#dataset with only 2 attributes
X, y = X_iris[:, :2], y_iris

#splitting between training(75%) and test(25%) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

#standardize
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

colors = ['red', 'greenyellow', 'blue']
for i in xrange(len(colors)):
    xs = X_train[:, 0][y_train == i]
    ys = X_train[:, 1][y_train == i]
    plt.scatter(xs, ys, c=colors[i])

plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
#plt.show()

from sklearn.linear_model import SGDClassifier
import numpy as np

clf = SGDClassifier()
clf.fit(X_train, y_train)
print clf.coef_
print '-----------------------------------'
print clf.intercept_

x_min, x_max = X_train[:, 0].min(), X_train[:, 0].max()
y_min, y_max = X_train[:, 1].min(), X_train[:, 1].max()
x_min -= .5
x_max += .5
y_min -= .5
y_max += .5

xs = np.arange(x_min, x_max, 0.5)
fig, axes = plt.subplots(1, 3)
fig.set_size_inches(10, 6)

for i in [0, 1, 2]:
    axes[i].set_aspect('equal')
    axes[i].set_title('Class' + str(i) + ' versus the rest')
    axes[i].set_xlabel('Sepal length')
    axes[i].set_ylabel('Sepal width')
    axes[i].set_xlim(x_min, x_max)
    axes[i].set_ylim(y_min, y_max)
    plt.sca(axes[i])
    for j in xrange(len(colors)):
        px = X_train[:, 0][y_train == j]
        py = X_train[:, 1][y_train == j]
        plt.scatter(px, py, c=colors[j])
    ys = ( -clf.intercept_[i] - xs * clf.coef_[i, 0]) / clf.coef_[i, 1]
    plt.plot(xs, ys, hold=True)
    
plt.show()

#new iris 4.7, 3.1
print clf.predict(scaler.transform([[4.7, 3.1]])) 

#distance from boundary line to  instance
print clf.decision_function(scaler.transform([[4.7, 3.1]]))

# Evaluating Results
from sklearn import metrics

#calculating accuracy on training set --> Wrong
y_train_pred = clf.predict(X_train)
print metrics.accuracy_score(y_train, y_train_pred)

#Calculating accuracy on test set --> apropriated
y_pred = clf.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)

#table of confusion
print metrics.classification_report(y_test, y_pred, target_names = iris.target_names)

print metrics.confusion_matrix(y_test, y_pred)
