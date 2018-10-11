# Installing sklearn and matplotlib modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
iris = pd.read_csv('iris.csv')
from sklearn.svm import SVC
X = iris[['sepal length', 'sepal width', 'petal length', 'petal width']]
y = iris['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
svm = SVC(kernel='rbf') # Fitting the model using rbf
svm.fit(X_train, y_train) # Fitting the model using training data
print('Accuracy of SVM classifier on training set: {:.2f}' # Accuracy on the training data
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}' # Accuracy on the testing data
     .format(svm.score(X_test, y_test)))