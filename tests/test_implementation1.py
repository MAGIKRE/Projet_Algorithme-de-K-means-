import pytest
from implementations.implementation1 import KMeansBasic

data = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]

def test_kmeans_basic():
    model = KMeansBasic(k=2)
    clusters = model.fit(data)
    assert len(clusters) == 2  # Vérifie que 2 clusters sont créés
    assert model.centroids is not None
