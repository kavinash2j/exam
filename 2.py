# Perform the following operations using Python on the Telecom_Churn
# dataset. Compute and display summary statistics for each feature available
# in the dataset using separate commands for each statistic. (e.g. minimum
# value, maximum value, mean, range, standard deviation, variance and
# percentiles).

import pandas as pd

# Load the dataset
df = pd.read_csv("Telecom Churn.csv")

# Select only numeric columns (exclude boolean)
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Minimum value of each feature
print("Minimum values:")
print(df.min(), "\n")

# Maximum value of each feature
print("Maximum values:")
print(df.max(), "\n")

# Mean of each feature
print("Mean values:")
print(numeric_df.mean(), "\n")

# Range of each feature (max - min)
print("Range of each feature:")
print(numeric_df.max() - numeric_df.min(), "\n")

# Standard deviation of each feature
print("Standard Deviation:")
print(numeric_df.std(), "\n")

# Variance of each feature
print("Variance:")
print(numeric_df.var(), "\n")

# Percentiles (25%, 50%, 75%)
print("25th Percentile:")
print(numeric_df.quantile(0.25), "\n")

print("50th Percentile (Median):")
print(numeric_df.quantile(0.50), "\n")

print("75th Percentile:")
print(numeric_df.quantile(0.75), "\n")
