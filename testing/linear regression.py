
# importing library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing dataset
dataset=pd.read_csv('Data.csv')

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

# Encoding the Categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
X=ct.fit_transform(x)
print(x)
# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

# Training the Simple Linear Regression model on the training set

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(X_train,y_train)

print(X_train)
# print(x_test)
# print(y_train)
# print(y_test)
# prediction on test set
y_pred=regressor.predict(X_test)
print(y_pred)
print(np.concatenate((y_pred.reshape(y_pred),1),y_test.reshape(len(y_test),1)))

