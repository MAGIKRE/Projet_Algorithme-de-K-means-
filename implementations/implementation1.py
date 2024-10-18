import random
import math

class KMeansBasic:
    def __init__(self, k, max_iter=100):
        self.k = k
        self.max_iter = max_iter
        self.centroids = []

    def initialize_centroids(self, data):
        self.centroids = random.sample(data, self.k)

    def assign_clusters(self, data):
        clusters = [[] for _ in range(self.k)]
        for point in data:
            closest_centroid_idx = self.closest_centroid(point)
            clusters[closest_centroid_idx].append(point)
        return clusters

    def closest_centroid(self, point):
        distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
        return distances.index(min(distances))

    def update_centroids(self, clusters):
        new_centroids = []
        for cluster in clusters:
            new_centroid = [sum(x)/len(cluster) for x in zip(*cluster)]
            new_centroids.append(new_centroid)
        return new_centroids

    def euclidean_distance(self, point1, point2):
        return math.sqrt(sum([(x - y) ** 2 for x, y in zip(point1, point2)]))

    def fit(self, data):
        self.initialize_centroids(data)
        for _ in range(self.max_iter):
            clusters = self.assign_clusters(data)
            new_centroids = self.update_centroids(clusters)
            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids
        return clusters

    def predict(self, data):
        return [self.closest_centroid(point) for point in data]
