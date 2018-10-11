######################################################
# a. Apply SVC with kernel “poly” degree =4
# Importing Libraries
import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
iris = pd.read_csv('iris.csv') # Reading Iris data
from sklearn.svm import SVC # Importing SVC from the sklearn
X = iris[['sepal length', 'sepal width', 'petal length', 'petal width']] # The input data or independent variables
y = iris['class'] # The dependent variable
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
svm = SVC(kernel='poly', degree=4) # The SVM model using poly, degree 4
svm.fit(X_train, y_train) # Fitting the model on the training dataset
print('Accuracy of SVM classifier on training set: {:.2f}' # Printing the accuracy on the training dataset
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}' # Printing the accuracy on the testing dataset
     .format(svm.score(X_test, y_test)))

