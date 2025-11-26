import numpy as np
import pandas as pd

# Load dataset (assumes IRIS.csv is in the working directory)
df = pd.read_csv("IRIS.csv")

# Features to use for clustering
features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
X = df[features].values.astype(float)

# K-means parameters
k = 4
iterations = 10
random_seed = 42

rng = np.random.default_rng(random_seed)
n_samples = X.shape[0]

# Initialize centroids by randomly picking k distinct data points
initial_idx = rng.choice(n_samples, size=k, replace=False)
centroids = X[initial_idx].copy()

print("Initial centroids (chosen from data points):")
for i, c in enumerate(centroids, start=1):
    print(f" m{i} = {np.round(c, 5)}")
print()

# K-means iterations
for it in range(1, iterations + 1):
    # Compute squared Euclidean distances (n_samples x k)
    dists = np.sum((X[:, np.newaxis, :] - centroids[np.newaxis, :, :]) ** 2, axis=2)

    # Assign each point to nearest centroid
    labels = np.argmin(dists, axis=1)

    # Recompute centroids
    new_centroids = np.zeros_like(centroids)
    for j in range(k):
        members = X[labels == j]
        if len(members) == 0:
            # Reinitialize empty centroid to a random data point
            new_centroids[j] = X[rng.integers(0, n_samples)]
        else:
            new_centroids[j] = members.mean(axis=0)

    centroids = new_centroids

    cluster_sizes = [int((labels == j).sum()) for j in range(k)]
    print(f"Iteration {it:2d}: cluster sizes = {cluster_sizes}")

print("\nFinal cluster centroids after", iterations, "iterations:")
for i, c in enumerate(centroids, start=1):
    print(f" m{i} = {np.round(c, 5)}")
