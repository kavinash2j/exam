# Write a program to do the following: You have given a collection of 8
# points. P1=[2, 10] P2=[2, 5] P3=[8, 4] P4=[5, 8] P5=[7,5] P6=[6, 4] P7=[1, 2]
# P8=[4, 9]. Perform the k-mean clustering with initial centroids as m1=P1
# =Cluster#1=C1 and m2=P4=cluster#2=C2, m3=P7 =Cluster#3=C3. Answer
# the following 1] Which cluster does P6 belong to? 2] What is the
# population of a cluster around m3? 3] What is the updated value of m1,
# m2, m3


import math

# Points
points = {
    'P1': (2, 10),
    'P2': (2, 5),
    'P3': (8, 4),
    'P4': (5, 8),
    'P5': (7, 5),
    'P6': (6, 4),
    'P7': (1, 2),
    'P8': (4, 9)
}

# Initial centroids
m1 = points['P1']   # C1
m2 = points['P4']   # C2
m3 = points['P7']   # C3

def euclid(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

# Assign each point to nearest centroid
assignments = {}
for name, pt in points.items():
    d1 = euclid(pt, m1)
    d2 = euclid(pt, m2)
    d3 = euclid(pt, m3)
    # choose nearest centroid (ties resolved by order m1, m2, m3)
    dists = [(d1, 'C1'), (d2, 'C2'), (d3, 'C3')]
    dists.sort(key=lambda x: x[0])
    cluster = dists[0][1]
    assignments[name] = {'point': pt, 'd1': d1, 'd2': d2, 'd3': d3, 'cluster': cluster}

# Print distance table (optional)
print("Point    (x,y)      d1       d2       d3    Cluster")
for name, info in assignments.items():
    pt = info['point']
    print(f"{name:3s}  {pt!s:10s}  {info['d1']:6.5f}  {info['d2']:6.5f}  {info['d3']:6.5f}   {info['cluster']}")

# 1) Which cluster does P6 belong to?
p6_cluster = assignments['P6']['cluster']
print("\n1) P6 belongs to:", p6_cluster)

# 2) Population of cluster around m3 (C3)
pop_m3 = sum(1 for v in assignments.values() if v['cluster'] == 'C3')
print("2) Population of cluster around m3 (C3):", pop_m3)

# 3) Updated centroids (mean of assigned points)
clusters = {'C1': [], 'C2': [], 'C3': []}
for name, info in assignments.items():
    clusters[info['cluster']].append(info['point'])

def mean_point(pts):
    x = sum(p[0] for p in pts) / len(pts)
    y = sum(p[1] for p in pts) / len(pts)
    return (round(x, 5), round(y, 5))

m1_new = mean_point(clusters['C1'])
m2_new = mean_point(clusters['C2'])
m3_new = mean_point(clusters['C3'])

print("3) Updated centroids:")
print("   m1 =", m1_new, "  (members:", clusters['C1'], ")")
print("   m2 =", m2_new, "  (members:", clusters['C2'], ")")
print("   m3 =", m3_new, "  (members:", clusters['C3'], ")")
