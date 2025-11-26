# Write a program to do the following: You have given a collection of 8
# points. P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85]
# P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. Perform the k-mean
# clustering with initial centroids as m1=P1 =Cluster#1=C1 and
# m2=P8=cluster#2=C2. Answer the following 1] Which cluster does P6
# belong to? 2] What is the population of a cluster around m2? 3] What is
# the updated value of m1 and m2



import math

points = {
    'P1': (0.1, 0.6),
    'P2': (0.15, 0.71),
    'P3': (0.08, 0.9),
    'P4': (0.16, 0.85),
    'P5': (0.2, 0.3),
    'P6': (0.25, 0.5),
    'P7': (0.24, 0.1),
    'P8': (0.3, 0.2)
}

m1 = points['P1']   # initial centroid 1
m2 = points['P8']   # initial centroid 2

def euclid(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

assignments = {}
for name, pt in points.items():
    d1 = euclid(pt, m1)
    d2 = euclid(pt, m2)
    cluster = 1 if d1 <= d2 else 2
    assignments[name] = {'point':pt, 'd1':d1, 'd2':d2, 'cluster':cluster}

# Which cluster P6 belongs to
p6_cluster = assignments['P6']['cluster']

# Population of cluster around m2 (cluster 2)
pop_m2 = sum(1 for v in assignments.values() if v['cluster']==2)

# Updated centroids (mean of points in each cluster)
cluster1_pts = [v['point'] for v in assignments.values() if v['cluster']==1]
cluster2_pts = [v['point'] for v in assignments.values() if v['cluster']==2]

def mean_point(pts):
    x = sum(p[0] for p in pts)/len(pts)
    y = sum(p[1] for p in pts)/len(pts)
    return (round(x,5), round(y,5))

m1_new = mean_point(cluster1_pts)
m2_new = mean_point(cluster2_pts)

print("P6 belongs to Cluster #", p6_cluster)
print("Population of cluster around m2 (cluster #2):", pop_m2)
print("Updated centroids: m1 =", m1_new, " m2 =", m2_new)
print("Cluster 1 members:", [name for name,v in assignments.items() if v['cluster']==1])
print("Cluster 2 members:", [name for name,v in assignments.items() if v['cluster']==2])
