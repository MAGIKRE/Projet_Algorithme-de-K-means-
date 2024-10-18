import pytest
import numpy as np
from implementations.implementation2 import KMeansOptimized

data = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

def test_kmeans_optimized():
    model = KMeansOptimized(k=2)
    clusters = model.fit(data)
    assert len(np.unique(clusters)) == 2  # Vérifie que 2 clusters sont créés
    assert model.centroids is not None
