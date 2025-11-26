# Perform the following operations using Python on the data set
# House_Price Prediction dataset. Compute standard deviation, variance and
# percentiles using separate commands, for each feature. Create a histogram
# for each feature in the dataset to illustrate the feature distributions.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("House Data.csv")

# ---------- Standard Deviation ----------
print("Standard Deviation:")
print(df.std(numeric_only=True))
print("\n")

# ---------- Variance ----------
print("Variance:")
print(df.var(numeric_only=True))
print("\n")

# ---------- Percentiles ----------
print("25th Percentile:")
print(df.quantile(0.25, numeric_only=True))
print("\n")

print("50th Percentile (Median):")
print(df.quantile(0.50, numeric_only=True))
print("\n")

print("75th Percentile:")
print(df.quantile(0.75, numeric_only=True))
print("\n")

# ---------- Histograms for each feature ----------
df.hist(figsize=(15, 12))
plt.tight_layout()
plt.show()
