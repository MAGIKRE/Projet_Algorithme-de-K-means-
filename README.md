# Projet_Algorithme-de-K-means-# Projet Algorithme de K-means

## Description du Projet

Ce projet implémente l'algorithme **K-means** en Python, une méthode de clustering utilisée pour partitionner des données en k groupes en fonction de leurs caractéristiques. 

L'objectif du projet est de :

1. Implémenter l'algorithme K-means de deux manières différentes, en utilisant des structures de données distinctes pour obtenir des complexités différentes.
2. Appliquer les principes de la **Programmation Orientée Objet (POO)** pour structurer l'implémentation.
3. Écrire des **tests unitaires** pour valider les implémentations à l'aide de `pytest`.
4. Visualiser graphiquement le fonctionnement de l'algorithme avec `matplotlib`.
5. Analyser les **complexités temporelles** et **spatiales** des deux implémentations et comparer leurs performances.

## Algorithme de K-means

L'algorithme de K-means partitionne des points de données en **k clusters**, où chaque point appartient au cluster dont la moyenne des caractéristiques (centroïde) est la plus proche. Le processus est itératif et suit les étapes suivantes :

1. Choisir **k** points de départ pour les centres (centroïdes) des clusters.
2. Assigner chaque point de données au centroïde le plus proche.
3. Recalculer les centroïdes en prenant la moyenne des points assignés à chaque cluster.
4. Répéter les étapes 2 et 3 jusqu'à ce que les centroïdes ne changent plus.

## Arborescence du Projet

Le projet est organisé selon l'arborescence suivante :

projet-algorithme/
├── README.md
├── main.py
├── descriptions/
│   └── description_simple.md
├── implementations/
│   ├── implementation1.py
│   └── implementation2.py
├── tests/
│   ├── test_implementation1.py
│   └── test_implementation2.py
├── visualisations/
│   └── visualisation.py
├── analyses/
│   └── analyse_complexite.md
└── ressources/
    └── [données, images, etc.]


### Détails des dossiers

- **`main.py`** : Le script principal pour exécuter le programme.
- **`descriptions/`** : Contient la description simple de l'algorithme K-means.
- **`implementations/`** : Contient les deux implémentations différentes de l'algorithme.
- **`tests/`** : Contient les tests unitaires pour chaque implémentation.
- **`visualisations/`** : Contient la représentation graphique de l'algorithme.
- **`analyses/`** : Contient l'analyse des complexités temporelles et spatiales.

## Installation

### Prérequis

Assurez-vous d'avoir Python 3.x installé sur votre machine. Voici les dépendances utilisées dans ce projet :

- `matplotlib` : Pour la visualisation graphique.
- `pytest` : Pour les tests unitaires.

### Installation des dépendances

Vous pouvez installer les dépendances avec `pip` :

```bash
pip install matplotlib pytest

