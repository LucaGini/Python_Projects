import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#Sample data
X = np.array([[2,50],[4,70],[6,80],[8,90],[10,85],
              [1,40],[3,60],[5,75],[7,80],[9,95]]) #Features
y = np.array([0,0,1,1,1,0,0,1,1,1]) #0:Fails 1:Passes

#Split the data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42) #Split the data 70-30

#Create and train the model
model = LogisticRegression()
model.fit(X_train,y_train)

#Make predictions
y_pred = model.predict(X_test)

#Evaluate the model
accuracy = accuracy_score(y_test,y_pred)
conf_matrix = confusion_matrix(y_test,y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion matrix: \n{conf_matrix}")

#Predict the outcome for a new student
new_student = np.array([[5,75]])
prediction = model.predict(new_student)
print(f"Prediction for new student: {'Pass' if prediction[0] == 1 else 'Fail'}")

#Plot the decision boundary
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#Create a meshgrid
h = 0.1
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
xx, yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

#Predict the class for each point in the meshgrid
Z = model.predict(np.c_[xx.ravel(),yy.ravel()])
Z = Z.reshape(xx.shape)

#Plot the decision boundary
plt.figure()
plt.pcolormesh(xx,yy,Z,cmap=ListedColormap(['#FFAAAA','#AAAAFF']))
plt.scatter(X[y==0][:,0],X[y==0][:,1],color='red',label='Fail')
plt.scatter(X[y==1][:,0],X[y==1][:,1],color='blue',label='Pass')
plt.xlabel('Hours studied')
plt.ylabel('Score')

plt.legend()
plt.show()