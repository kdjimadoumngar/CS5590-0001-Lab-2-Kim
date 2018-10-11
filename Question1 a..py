# 1.Pick any dataset from the dataset sheet in the class sheet
# a. plot how many of each category is available in your dataset you can use seaborn library or matplotlib)
# b. createone prediction model based on Naïve Bayes Classification and evaluate your model

# Importing Libraries
import numpy as np # Import numpy
import pandas as pd #Importing pandas
import matplotlib.pyplot as plt # Importing matplotlib

import seaborn as sns # Import season

iris = pd.read_csv('iris.csv') # Loading Iris data
print(iris.head()) # Printing column headers
print(iris['class'].unique()) # Printing classes
print(iris.describe()) # Print the class descriptions
sns.countplot(iris['class'],label="Count") # Plotting the categories and show the plot
plt.show()