# . Write a program to cluster a set of points using K-means for IRIS
# dataset. Consider, K=3, clusters. Consider Euclidean distance as the
# distance measure. Randomly initialize a cluster mean as one of the data
# points. Iterate at least for 10 iterations. After iterations are over, print the
# final cluster means for each of the clusters


# ---------------------------------------------------------
# K-MEANS CLUSTERING on IRIS DATASET (EASY VERSION)
# K = 3, Euclidean distance, 10 iterations
# ---------------------------------------------------------

import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. LOAD IRIS DATASET (ONLY NUMERIC COLUMNS)
# ---------------------------------------------------------
df = pd.read_csv("IRIS.csv")

# We pick 4 numeric features
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].values

# Number of clusters
k = 3

# Total number of iterations
iterations = 10

# ---------------------------------------------------------
# 2. RANDOMLY PICK 3 POINTS AS INITIAL CENTROIDS
# ---------------------------------------------------------
np.random.seed(42)               # for same result every run
n = X.shape[0]                   # total rows in dataset
idx = np.random.choice(n, k, replace=False)   # choose 3 random indices

centroids = X[idx].copy()        # initial centroids

print("Initial Centroids:")
for i, c in enumerate(centroids, start=1):
    print(f"m{i} =", c)
print()

# ---------------------------------------------------------
# 3. FUNCTION TO CALCULATE EUCLIDEAN DISTANCE
# ---------------------------------------------------------
def euclidean(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# ---------------------------------------------------------
# 4. MAIN K-MEANS LOOP (RUN 10 ITERATIONS)
# ---------------------------------------------------------
for it in range(1, iterations + 1):

    # Step A: Assign each point to nearest centroid
    labels = []          # will store cluster number for each point

    for p in X:
        # compute distance of this point to m1, m2, m3
        dists = [euclidean(p, c) for c in centroids]
        # choose nearest centroid index
        labels.append(np.argmin(dists))

    labels = np.array(labels)

    # Step B: Recompute centroids as mean of points inside each cluster
    new_centroids = []

    for j in range(k):
        cluster_points = X[labels == j]   # all points assigned to cluster j

        if len(cluster_points) == 0:
            # if a cluster becomes empty, reassign randomly
            new_centroids.append(X[np.random.randint(0, n)])
        else:
            # average of all points in this cluster → new centroid
            new_centroids.append(cluster_points.mean(axis=0))

    centroids = np.array(new_centroids)

    # Show cluster sizes for each iteration
    sizes = [np.sum(labels == j) for j in range(k)]
    print(f"Iteration {it} - Cluster sizes:", sizes)

# ---------------------------------------------------------
# 5. PRINT FINAL CLUSTER MEANS
# ---------------------------------------------------------
print("\nFinal Centroids After 10 Iterations:")
for i, c in enumerate(centroids, start=1):
    print(f"m{i} =", np.round(c, 4))
