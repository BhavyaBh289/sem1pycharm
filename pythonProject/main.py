
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import metrics
import seaborn as sns

"""Importing csv file """

dataset = pd.read_csv("survey lung cancer.csv")
print(dataset)
print(dataset.head())
print(dataset.info())

dataset.GENDER.value_counts(normalize=True)*100

"""Data modification"""

labelencoder = LabelEncoder()
dataset["LUNG_CANCER"] =labelencoder.fit_transform(dataset["LUNG_CANCER"])
dataset["GENDER"] =labelencoder.fit_transform(dataset["GENDER"])
print(dataset)

"""Data Visualisation"""

sns.distplot(a=dataset["AGE"]);

r = dataset.groupby('LUNG_CANCER')['LUNG_CANCER'].count()
plt.pie(r, explode=[0.05, 0.1], labels=['No', 'Yes'], radius=1.5, autopct='%1.1f%%', shadow=True);

fig, axes = plt.subplots(4, 4, figsize=(25, 15))
fig.suptitle('Different feature distributions')
axes = axes.reshape(16,)
for i,column in enumerate(dataset.columns):
  sns.histplot(ax = axes[i],data = dataset, x= column)

"""Splitting data into test and training"""

xtrain,xtest,ytrain,ytest=train_test_split(dataset[['SMOKING']],dataset.LUNG_CANCER,test_size=0.25,random_state=27)

"""Logistic Regression"""

lr = LogisticRegression()
lr.fit(xtrain, ytrain)
y_pred = lr.predict(xtest)

"""Calculate Accuracy """

lr_train_acc = accuracy_score(ytrain, lr.predict(xtrain))
lr_test_acc = accuracy_score(ytest, y_pred)
print(f"Training Accuracy of Logistic Regression Model is {lr_train_acc*100}")
print(f"Test Accuracy of Logistic Regression Model is {lr_test_acc*100}")

confusion_matrix(ytest, y_pred)