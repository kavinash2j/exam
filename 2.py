import pandas as pd

# Load the dataset
df = pd.read_csv("Telecom_Churn.csv")

# Minimum value of each feature
print("Minimum values:")
print(df.min(), "\n")

# Maximum value of each feature
print("Maximum values:")
print(df.max(), "\n")

# Mean of each feature
print("Mean values:")
print(df.mean(numeric_only=True), "\n")

# Range of each feature (max - min)
print("Range of each feature:")
print(df.max(numeric_only=True) - df.min(numeric_only=True), "\n")

# Standard deviation of each feature
print("Standard Deviation:")
print(df.std(numeric_only=True), "\n")

# Variance of each feature
print("Variance:")
print(df.var(numeric_only=True), "\n")

# Percentiles (25%, 50%, 75%)
print("25th Percentile:")
print(df.quantile(0.25, numeric_only=True), "\n")

print("50th Percentile (Median):")
print(df.quantile(0.50, numeric_only=True), "\n")

print("75th Percentile:")
print(df.quantile(0.75, numeric_only=True), "\n")
