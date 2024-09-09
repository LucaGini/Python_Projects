import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Sample data
X = np.array([[25,40000],[35,60000],[45,80000],[20,20000],[50,100000],
              [30,50000],[40,70000],[55,110000],[22,30000],[48,90000]]) #Features
y = np.array([0,1,1,0,1,0,1,1,0,1]) #0: No purchase 1: Purchase

#Split the data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42) #Split the data

#Create and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)

#Make predictions
y_pred = model.predict(X_test)

#Evaluate the model
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy}")

#Visualize the decision tree
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=['Age', 'Salary'], class_names=['No purchase','Purchase'], filled=True)
plt.show()

#Predict the outcome for a new customer
new_customer = np.array([[28,55000]])
prediction = model.predict(new_customer)
print(f"Prediction for new customer: {'Purchase' if prediction[0] == 1 else 'No purchase'}")