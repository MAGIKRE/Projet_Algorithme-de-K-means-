import numpy as np

class KMeansOptimized:
    def __init__(self, k, max_iter=100):
        self.k = k
        self.max_iter = max_iter
        self.centroids = None

    def initialize_centroids(self, data):
        indices = np.random.choice(data.shape[0], self.k, replace=False)
        self.centroids = data[indices]

    def assign_clusters(self, data):
        distances = np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def update_centroids(self, data, clusters):
        new_centroids = np.array([data[clusters == k].mean(axis=0) for k in range(self.k)])
        return new_centroids

    def fit(self, data):
        self.initialize_centroids(data)
        for _ in range(self.max_iter):
            clusters = self.assign_clusters(data)
            new_centroids = self.update_centroids(data, clusters)
            if np.all(new_centroids == self.centroids):
                break
            self.centroids = new_centroids
        return clusters

    def predict(self, data):
        return self.assign_clusters(data)
