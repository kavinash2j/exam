# Perform the following operations using Python on a suitable data set,
# counting unique values of data, format of each column, converting variable
# data type (e.g. from long to short, vice versa), identifying missing values
# and filling in the missing values.

import pandas as pd
import numpy as np

# Load the Titanic dataset
df = pd.read_csv("Titanic.csv")

# -----------------------------------------------
# 1. COUNT UNIQUE VALUES IN EACH COLUMN
# -----------------------------------------------
print("=== UNIQUE VALUE COUNT (PER COLUMN) ===")
print(df.nunique(dropna=False))
print("\n")

# -----------------------------------------------
# 2. FORMAT / DATA TYPE OF EACH COLUMN
# -----------------------------------------------
print("=== COLUMN DATA TYPES ===")
print(df.dtypes)
print("\n")

# -----------------------------------------------
# 3. CONVERT VARIABLE DATA TYPES
# (examples: int64→int32, float64→float32, object→category)
# -----------------------------------------------

# Convert numeric columns to smaller types
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    if pd.api.types.is_integer_dtype(df[col]):
        df[col] = pd.to_numeric(df[col], downcast="integer")
    else:
        df[col] = pd.to_numeric(df[col], downcast="float")

# Convert string/object columns to category type
for col in df.select_dtypes(include=["object"]).columns:
    if df[col].nunique() < len(df) * 0.5:   # convert low-cardinality
        df[col] = df[col].astype("category")

print("=== DATA TYPES AFTER CONVERSION ===")
print(df.dtypes)
print("\n")

# -----------------------------------------------
# 4. IDENTIFY MISSING VALUES
# -----------------------------------------------
print("=== MISSING VALUES (PER COLUMN) ===")
print(df.isnull().sum())
print("\n")

print("=== ROWS WITH MISSING VALUES (FIRST 10) ===")
print(df[df.isnull().any(axis=1)].head(10))
print("\n")

# -----------------------------------------------
# 5. FILL MISSING VALUES
# Numeric: median
# Categorical: mode
# -----------------------------------------------

# Fill numeric missing values
numeric_cols = df.select_dtypes(include=["number"]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values
cat_cols = df.select_dtypes(include=["category", "object"]).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Verify all missing values are filled
print("=== TOTAL MISSING VALUES AFTER CLEANING ===")
print(df.isnull().sum().sum(), "missing values remain\n")

# -----------------------------------------------
# 6. OPTIONAL: SHOW SUMMARY STATISTICS
# -----------------------------------------------
print("=== SUMMARY STATISTICS (NUMERIC) ===")
print(df.describe())
