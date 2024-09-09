from sklearn.manifold import TSNE
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

#Load the digits dataset
digits = load_digits()
X = digits.data
y = digits.target

#Perform t-SNE
tsne = TSNE(n_components=2, random_state=42) #Reduce the data to 2 dimensions
X_tsne = tsne.fit_transform(X) 

#Plot the results
plt.figure(figsize=(10,8))
scatter = plt.scatter(X_tsne[:,0],X_tsne[:,1],c=y,cmap='viridis')
plt.colorbar(scatter)
plt.xlabel('t-SNE feature 1')
plt.ylabel('t-SNE feature 2')
plt.title('t-SNE Visualization of MNIST digits')
plt.show()

#Print some statistics
print(f"Original data shape: {X.shape}")
print(f"t-SNE reduced data shape: {X_tsne.shape}")