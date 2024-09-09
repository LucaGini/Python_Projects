import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

#Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

#Perform PCA
pca = PCA(n_components=2) #Reduce the data to 2 dimensions
X_pca = pca.fit_transform(X)

#Plot the results
plt.figure(figsize=(10,8))
for i, target_name in enumerate(iris.target_names):
    plt.scatter(X_pca[y==i,0],X_pca[y==i,1],label=target_name)
    
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.title('PCA of Iris dataset')
plt.show()

#Print the explained variance ratio
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")