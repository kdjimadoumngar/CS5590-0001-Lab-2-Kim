# import csv
#
# myData = 'iris.csv'
#
# dataset = csv.reader(myData)
#
#
# def loadCsv(filename):
#
#     for i in range(len(dataset)):
#         dataset[i] = [float(x) for x in dataset[i]]
#     return dataset

# Loading iris data



#print('Loaded data file {0} with {1} rows').format(myData, len(dataset))

##############################################################
# #Naive Bayse (Gaussian)
#
from sklearn import datasets

from sklearn import metrics

from sklearn.naive_bayes import GaussianNB

#Loading iris data

dataset = datasets.load_iris()


# Fitting NB Model to the data

lm = GaussianNB()

lm.fit(dataset.data, dataset.target)

print(lm)

# Making prediction

exp = dataset.target

pred = lm.predict(dataset.data)

# Summary of the fitted model

print(metrics.classification_report(exp, pred))

print(metrics.confusion_matrix(exp, pred))

######################################################################





