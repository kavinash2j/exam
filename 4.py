#  Write a program to do: A dataset collected in a cosmetics shop showing
# details of customers and whether or not they responded to a special offer
# to buy a new lip-stick is shown in table below. (Implement step by step
# using commands - Dont use library) Use this dataset to build a decision
# tree, with Buys as the target variable, to help in buying lipsticks in the
# future. Find the root node of the decision tree


# ID3-style information gain calculation WITHOUT external libraries
# - Reads dataset from "Lipstick.csv" (must be in same folder)
# - Assumes last column is the target "Buys" (or uses header name)
# - Computes entropy and information gain for each attribute
# - Prints information gain values and the chosen root attribute

import csv
import math
from collections import Counter, defaultdict

def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [row for row in reader if any(cell.strip() != "" for cell in row)]
    return header, rows

def entropy_from_counts(counts):
    total = sum(counts)
    ent = 0.0
    for c in counts:
        if c == 0:
            continue
        p = c / total
        ent -= p * math.log2(p)
    return ent

def entropy_of_list(values):
    counts = list(Counter(values).values())
    return entropy_from_counts(counts)

def information_gain(rows, col_index, target_index):
    # base entropy
    target_vals = [r[target_index] for r in rows]
    base_ent = entropy_of_list(target_vals)
    # partition by attribute values
    partitions = defaultdict(list)
    for r in rows:
        partitions[r[col_index]].append(r[target_index])
    total = len(rows)
    remainder = 0.0
    for subset in partitions.values():
        weight = len(subset) / total
        remainder += weight * entropy_of_list(subset)
    return base_ent - remainder

def main():
    path = "Lipstick.csv"   # change path if needed
    header, rows = read_csv(path)
    # normalize header names
    header = [h.strip() for h in header]
    # If header includes 'Buys', use that as target; otherwise assume last column
    if "Buys" in header:
        target_index = header.index("Buys")
    else:
        target_index = len(header) - 1

    print("Attributes (columns):", header)
    print("Using target column:", header[target_index], " (index", target_index, ")")
    print("Total records:", len(rows))
    print()

    gains = {}
    for i, col in enumerate(header):
        if i == target_index:
            continue
        g = information_gain(rows, i, target_index)
        gains[col] = g

    print("Information Gain for each attribute:")
    for attr, g in gains.items():
        print(f" - {attr}: {g:.6f}")

    # select root attribute (highest gain)
    root_attr = max(gains, key=gains.get)
    print("\nSelected root node (attribute with highest information gain):", root_attr)

if __name__ == "__main__":
    main()
