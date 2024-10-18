from implementations.implementation1 import KMeansBasic
from implementations.implementation2 import KMeansOptimized
import numpy as np

# Données d'exemple
data = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
data_np = np.array(data)

# Implémentation de base
kmeans_basic = KMeansBasic(k=2)
clusters_basic = kmeans_basic.fit(data)
print("Implémentation 1 - Clusters:", clusters_basic)
print("Centroids:", kmeans_basic.centroids)

# Implémentation optimisée
kmeans_optimized = KMeansOptimized(k=2)
clusters_optimized = kmeans_optimized.fit(data_np)
print("Implémentation 2 - Clusters:", clusters_optimized)
print("Centroids:", kmeans_optimized.centroids)
