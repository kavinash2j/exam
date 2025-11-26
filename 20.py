import numpy as np
import pandas as pd

# Load the dataset (numeric columns only)
df = pd.read_csv("IRIS.csv")

# Select numeric feature columns
features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
X = df[features].values.astype(float)

# Parameters
k = 3
iterations = 10
random_seed = 42

rng = np.random.default_rng(random_seed)
n_samples = X.shape[0]

# Initialize centroids by picking k random points
initial_idx = rng.choice(n_samples, size=k, replace=False)
centroids = X[initial_idx].copy()

print("Initial centroids:")
for i, c in enumerate(centroids, start=1):
    print(f" m{i} = {np.round(c, 5)}")
print()

# K-means main loop
for it in range(1, iterations + 1):

    # Compute Euclidean distances to each centroid
    dists = np.sum((X[:, np.newaxis, :] - centroids[np.newaxis, :, :]) ** 2, axis=2)

    # Assign each point to nearest centroid
    labels = np.argmin(dists, axis=1)

    # Recompute centroids
    new_centroids = np.zeros_like(centroids)
    for j in range(k):
        members = X[labels == j]
        if len(members) == 0:
            new_centroids[j] = X[rng.integers(0, n_samples)]   # reassign empty cluster
        else:
            new_centroids[j] = members.mean(axis=0)

    centroids = new_centroids

    # Show cluster sizes during training
    cluster_sizes = [int((labels == j).sum()) for j in range(k)]
    print(f"Iteration {it:2d} → Cluster sizes: {cluster_sizes}")

# Final results
print("\nFinal centroids after 10 iterations:")
for i, c in enumerate(centroids, start=1):
    print(f" m{i} = {np.round(c, 5)}")
