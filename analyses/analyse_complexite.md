### Analyse de Complexité de l'Algorithme K-means

#### Rappel de l'Algorithme

L'algorithme K-means est une méthode de partitionnement des données en **k** groupes (ou clusters). L'idée est de regrouper les points de données en fonction de leurs similarités, avec chaque cluster représenté par son centroïde. Voici les étapes principales de K-means :

1. Initialisation de **k** centroïdes (soit aléatoirement, soit en utilisant une méthode spécifique comme K-means++).
2. Attribution de chaque point de données au cluster dont le centroïde est le plus proche.
3. Mise à jour des centroïdes en prenant la moyenne des points assignés à chaque cluster.
4. Répétition des étapes 2 et 3 jusqu'à ce que les centroïdes ne changent plus ou jusqu'à convergence.

---

### Complexité Temporelle

La complexité temporelle de l'algorithme K-means dépend de trois facteurs principaux :
- **n** : Nombre total de points de données.
- **k** : Nombre de clusters.
- **t** : Nombre d'itérations nécessaires pour que l'algorithme converge.

#### Étape 1 : Initialisation des centroïdes
- L'initialisation des centroïdes prend **O(k)** si elle est faite aléatoirement.
- Si une méthode comme **K-means++** est utilisée, l'initialisation est plus coûteuse et nécessite **O(n * k)** opérations.

#### Étape 2 : Assignation des points aux centroïdes
- Pour chaque point, on calcule sa distance avec chacun des **k** centroïdes, ce qui prend **O(k)** opérations par point.
- Avec **n** points à assigner, cette étape prend **O(n * k)** par itération.

#### Étape 3 : Recalcul des centroïdes
- Pour chaque cluster, le centroïde est recalculé en prenant la moyenne des coordonnées des points qui lui sont assignés. Cela nécessite un parcours de tous les points du cluster, donc **O(n)** opérations par itération.

#### Étape 4 : Répétition jusqu'à convergence
- L'algorithme K-means s'exécute sur **t** itérations jusqu'à ce que les centroïdes convergent. En général, **t** est beaucoup plus petit que **n**, mais dans le pire des cas, on le traite comme un paramètre dépendant des données.

Ainsi, la complexité temporelle totale de l'algorithme est :

\[
O(t * n * k)
\]

où :
- **n** est le nombre de points,
- **k** est le nombre de clusters,
- **t** est le nombre d'itérations jusqu'à convergence.

### Complexité Spatiale

La complexité spatiale du K-means est relativement simple. Elle dépend de :
1. **n** points de données, nécessitant **O(n)** espace.
2. **k** centroïdes, nécessitant **O(k)** espace.
3. L'affectation de chaque point à un cluster, nécessitant **O(n)** espace.

Ainsi, la complexité spatiale totale est :

\[
O(n + k)
\]

---

### Comparaison des Implémentations

#### Implémentation 1 : K-means Classique

Dans l'implémentation 1, nous utilisons l'algorithme K-means basique, où les centroïdes sont initialisés aléatoirement. Cette version suit le schéma classique sans aucune optimisation spécifique.

- **Complexité Temporelle** : **O(t * n * k)**.
- **Complexité Spatiale** : **O(n + k)**.

Avantages :
- Facile à implémenter et rapide à démarrer.
- Convient pour des jeux de données de taille modérée et pour des tâches où une précision optimale n'est pas critique.

Inconvénients :
- Le nombre d'itérations **t** peut être plus élevé en raison de la mauvaise initialisation aléatoire des centroïdes.
- Peut converger vers des minima locaux si l'initialisation n'est pas optimale.

#### Implémentation 2 : K-means++ (Optimisation de l'Initialisation)

Dans cette implémentation, nous utilisons **K-means++** pour initialiser les centroïdes de manière plus intelligente. L'algorithme K-means++ choisit des centroïdes de manière à maximiser la distance entre eux, ce qui accélère souvent la convergence.

- **Complexité Temporelle** : **O(t * n * k) + O(n * k)**. L'initialisation avec K-means++ ajoute un coût initial de **O(n * k)**, mais réduit généralement le nombre d'itérations **t** pour atteindre la convergence.
- **Complexité Spatiale** : **O(n + k)**.

Avantages :
- Meilleure initialisation, ce qui conduit souvent à une convergence plus rapide.
- Moins d'itérations nécessaires pour atteindre un bon résultat.

Inconvénients :
- Le coût d'initialisation est plus élevé (en **O(n * k)**), mais cela est compensé par un nombre réduit d'itérations **t**.

---

### Conclusion

Les deux implémentations de K-means que nous avons réalisées ont des caractéristiques distinctes :

1. **K-means Basique** : 
   - Avantage : Implémentation simple et rapide.
   - Inconvénient : Peut être plus lent à converger avec une initialisation aléatoire des centroïdes.

2. **K-means++** : 
   - Avantage : Une initialisation plus intelligente améliore la convergence et réduit souvent le nombre d'itérations.
   - Inconvénient : Le coût initial est plus élevé, mais cela est souvent compensé par un temps d'exécution total plus rapide.

En résumé, bien que l'implémentation avec **K-means++** soit plus coûteuse au départ, elle conduit généralement à de meilleures performances en termes de convergence, en particulier pour des jeux de données complexes.
