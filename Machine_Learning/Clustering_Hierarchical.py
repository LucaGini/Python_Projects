import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

#Sample data: Movie genre ratings (Action, Comedy, Drama, SciFi)
X = np.array([[8,2,4,7],
              [5,7,3,1],
              [2,8,7,2],
              [9,1,3,8],
              [3,6,9,2],
              [7,3,2,9]])

movie_names = ['The Avengers','The Hangover','The Notebook','Interstellar','The Martian','The Dark Knight']

#Perform hierarchical clustering
linkage_matrix = linkage(X,method='ward') #Generate the linkage matrix

#Plot the dendrogram
plt.figure(figsize=(10,7))
dendrogram(linkage_matrix,labels=movie_names)
plt.title('Movie Clustering Dendogram')
plt.xlabel('Movie')
plt.ylabel('Distance')
plt.show()

#Create clusters
n_clusters = 3
clustering = AgglomerativeClustering(n_clusters=n_clusters)
clustering.fit(X)

#Print results
for i in range(n_clusters):
    cluster_movies = [movie_names[j] for j in range(len(movie_names)) if clustering.labels_[j] == i]
    print(f"Cluster {i+1}: {', '.join(cluster_movies)}")