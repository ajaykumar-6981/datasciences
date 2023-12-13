
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing the dataset
dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

# Training the Linear Regreession model on the train set
from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(x,y)

# Predicting the test set
y_pred=regressor.predict(x)
print(np.set_printoptions(precision=2))
print(np.concatenate((y_pred.reshape(len(y_pred),1),x.reshape(len(x),1),1))


# Visualising the dataset
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x),color='blue')
plt.show()