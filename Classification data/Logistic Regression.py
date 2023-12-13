
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing the dataset
dataset=pd.read_csv('50_Startups.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

# Splitting the dataset into the Training set and test set

from sklearn.model_selection import train_test_split
X_train,y_train,X_test,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

print(X_train)
print(X_test)

