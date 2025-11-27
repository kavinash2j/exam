# Write a program to do the following: You have given a collection of 8
# points. P1=[2, 10] P2=[2, 5] P3=[8, 4] P4=[5, 8] P5=[7,5] P6=[6, 4] P7=[1, 2]
# P8=[4, 9]. Perform the k-mean clustering with initial centroids as m1=P1
# =Cluster#1=C1 and m2=P4=cluster#2=C2, m3=P7 =Cluster#3=C3. Answer
# the following 1] Which cluster does P6 belong to? 2] What is the
# population of a cluster around m3? 3] What is the updated value of m1,
# m2, m3


# K-Means (One Iteration) – Easy Version
import math

# Points
P1 = (2,10)
P2 = (2,5)
P3 = (8,4)
P4 = (5,8)
P5 = (7,5)
P6 = (6,4)
P7 = (1,2)
P8 = (4,9)

points = {"P1":P1,"P2":P2,"P3":P3,"P4":P4,"P5":P5,"P6":P6,"P7":P7,"P8":P8}

# Initial centroids
m1 = P1   # C1
m2 = P4   # C2
m3 = P7   # C3

# Distance function
def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Assign each point to nearest cluster
cluster = {}

for name, p in points.items():
    d1 = dist(p, m1)
    d2 = dist(p, m2)
    d3 = dist(p, m3)

    if d1 <= d2 and d1 <= d3:
        cluster[name] = "C1"
    elif d2 <= d1 and d2 <= d3:
        cluster[name] = "C2"
    else:
        cluster[name] = "C3"

# 1) Which cluster does P6 belong to?
print("1) P6 belongs to:", cluster["P6"])

# 2) Population of C3
pop_C3 = sum(1 for x in cluster.values() if x == "C3")
print("2) Population of cluster around m3 (C3):", pop_C3)

# 3) Updated centroids
C1_pts = [points[p] for p in cluster if cluster[p] == "C1"]
C2_pts = [points[p] for p in cluster if cluster[p] == "C2"]
C3_pts = [points[p] for p in cluster if cluster[p] == "C3"]

def mean(pts):
    x = sum(p[0] for p in pts) / len(pts)
    y = sum(p[1] for p in pts) / len(pts)
    return (round(x,2), round(y,2))

m1_new = mean(C1_pts)
m2_new = mean(C2_pts)
m3_new = mean(C3_pts)

print("3) Updated centroids:")
print("   m1 =", m1_new)
print("   m2 =", m2_new)
print("   m3 =", m3_new)
