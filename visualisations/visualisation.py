import matplotlib.pyplot as plt
import numpy as np
from implementations.implementation2 import KMeansOptimized

def plot_clusters(data, labels, centroids):
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='x')
    plt.show()

# Exemple d'utilisation
data = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
model = KMeansOptimized(k=2)
labels = model.fit(data)
plot_clusters(data, labels, model.centroids)
