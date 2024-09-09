import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Sample data
X = np.array([[15000,39],[15500,81],[16000,6],[16000,77],[17000,40],
              [18000,76],[19000,6],[19500,93],[20000,72],[21000,14],
              [21000,89],[23000,17],[25000,94],[30000,2],[33000,57],
              [33000,99],[35000,36],[38000,35],[45000,1],[47000,60]]) #Features

#Create and fit the model
kmeans = KMeans(n_clusters=3,random_state=42)
kmeans.fit(X)

#Get cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

#Plot the data
plt.scatter(X[:,0],X[:,1],c=labels,cmap='viridis')
plt.scatter(centers[:,0],centers[:,1],c='red',s=200,marker='x',linewidths=3)
plt.xlabel('Annual income ($)')
plt.ylabel('Spending score (1-100)')
plt.title('Customer segments')
plt.show()

#Predict cluster for a new customer
new_customer = np.array([[22000,50]])
prediction = kmeans.predict(new_customer) 
print(f"Predicted cluster for new customer: {prediction[0]}")