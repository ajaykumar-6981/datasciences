
# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing dataset
dataset=pd.read_csv('Social_Network_Ads.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

# Splitting the dataset into train set and test_set
from sklearn.model_selection import train_test_split
x_train, y_train,x_test,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

print('x-train :',x_train)
print('y-tain :',y_train)
print('x-test :',x_test)
print('y-test :',y_test)

# Training the Logistic Regression model on the training set

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,x_train)

# Predicting a new result

 # classifier.predict(sc.transform([[30,87000]]))

#Predicting the Test set result
y_pred=classifier.predict(x_test)
print(np.contenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

# Making the Training set results

# making a confusion Matrix
from sklearn.matrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
accuracy_score(y_test,y_pred)

# visualising the Training set results
from matplotlib.colors import ListedColormap
x_set,y_set=sc.inverse_transform(x_train),y_train
x1,x2=np.meshgrid(np.arange(start=x_set[:,0].min()))

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set))

# Visualising the Test set results
