# Write a program to do the following: You have given a collection of 8
# points. P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85]
# P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. Perform the k-mean
# clustering with initial centroids as m1=P1 =Cluster#1=C1 and
# m2=P8=cluster#2=C2. Answer the following 1] Which cluster does P6
# belong to? 2] What is the population of a cluster around m2? 3] What is
# the updated value of m1 and m2



# -----------------------------------------
# STEP 1: Define the 8 points
# -----------------------------------------
P1 = (2, 10)
P2 = (2, 5)
P3 = (8, 4)
P4 = (5, 8)
P5 = (7, 5)
P6 = (6, 4)
P7 = (1, 2)
P8 = (4, 9)

points = {"P1":P1,"P2":P2,"P3":P3,"P4":P4,"P5":P5,"P6":P6,"P7":P7,"P8":P8}

# -----------------------------------------
# STEP 2: Initial centroids as given
# -----------------------------------------
m1 = P1   # Cluster C1
m2 = P4   # Cluster C2
m3 = P7   # Cluster C3

# -----------------------------------------
# STEP 3: Distance function (Euclidean)
# -----------------------------------------
import math
def dist(p, m):
    return math.sqrt((p[0]-m[0])**2 + (p[1]-m[1])**2)

# -----------------------------------------
# STEP 4: Assign each point to nearest centroid
# -----------------------------------------
cluster_assign = {}

for name, p in points.items():
    d1 = dist(p, m1)
    d2 = dist(p, m2)
    d3 = dist(p, m3)

    # choose smallest distance
    min_d = min(d1, d2, d3)

    if min_d == d1:
        cluster_assign[name] = "C1"
    elif min_d == d2:
        cluster_assign[name] = "C2"
    else:
        cluster_assign[name] = "C3"

# -----------------------------------------
# STEP 5: Show cluster assignment table
# -----------------------------------------
print("Point  →  Cluster")
for p in cluster_assign:
    print(p, "→", cluster_assign[p])

# -----------------------------------------
# ANSWER 1: Which cluster does P6 belong to?
# -----------------------------------------
print("\n1) P6 belongs to:", cluster_assign["P6"])

# -----------------------------------------
# STEP 6: Population of Cluster C3 (around m3)
# -----------------------------------------
pop_C3 = sum(1 for c in cluster_assign.values() if c == "C3")
print("2) Population of cluster around m3 (C3):", pop_C3)

# -----------------------------------------
# STEP 7: Updated centroids
# (Take mean of all points in each cluster)
# -----------------------------------------
C1_points = [points[p] for p in cluster_assign if cluster_assign[p] == "C1"]
C2_points = [points[p] for p in cluster_assign if cluster_assign[p] == "C2"]
C3_points = [points[p] for p in cluster_assign if cluster_assign[p] == "C3"]

def mean(pts):
    x = sum(p[0] for p in pts) / len(pts)
    y = sum(p[1] for p in pts) / len(pts)
    return (round(x,2), round(y,2))

m1_new = mean(C1_points)
m2_new = mean(C2_points)
m3_new = mean(C3_points)

print("\n3) Updated Centroids:")
print("   m1 =", m1_new, "from", C1_points)
print("   m2 =", m2_new, "from", C2_points)
print("   m3 =", m3_new, "from", C3_points)
