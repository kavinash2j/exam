# Perform the following operations using Python on a suitable data set,
# counting unique values of data, format of each column, converting variable
# data type (e.g. from long to short, vice versa), identifying missing values
# and filling in the missing values.

# Simple Titanic: inspect types, uniques, convert types, find & fill missing values
import pandas as pd                     # data handling
import numpy as np                      # numerical helpers

# ---------------------------
# 0. Load data
# ---------------------------
df = pd.read_csv("Titanic.csv")         # read CSV into a DataFrame

# ---------------------------
# 1. Count unique values per column
# ---------------------------
print("Unique values per column:")
print(df.nunique(dropna=False))         # count unique (including NaN)
print()

# ---------------------------
# 2. Show current data types
# ---------------------------
print("Data types BEFORE conversion:")
print(df.dtypes)                        # show dtype of each column
print()

# ---------------------------
# 3. Convert / downcast data types (make them smaller / efficient)
#    - ints -> smaller int (e.g. int64 -> int32)
#    - floats -> smaller float (e.g. float64 -> float32)
#    - low-cardinality strings -> category
# ---------------------------
# Downcast numeric columns
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    if pd.api.types.is_integer_dtype(df[col].dropna()):
        df[col] = pd.to_numeric(df[col], downcast="integer")  # smaller integer
    else:
        df[col] = pd.to_numeric(df[col], downcast="float")    # smaller float

# Convert low-cardinality object columns to category
for col in df.select_dtypes(include=["object"]).columns:
    # if unique values are less than half the rows, convert to category
    if df[col].nunique(dropna=False) < 0.5 * len(df):
        df[col] = df[col].astype("category")

print("Data types AFTER conversion:")
print(df.dtypes)
print()

# ---------------------------
# 4. Identify missing values
# ---------------------------
print("Missing values per column:")
print(df.isnull().sum())               # count NaNs per column
print()
print("First 10 rows that contain any missing values:")
print(df[df.isnull().any(axis=1)].head(10))  # show sample rows with missing data
print()

# ---------------------------
# 5. Fill missing values
#    - numeric -> median
#    - categorical/object -> mode (most frequent)
# ---------------------------
# Fill numeric columns with median
num_cols = df.select_dtypes(include=["number"]).columns
for col in num_cols:
    median_val = df[col].median()      # compute median (ignores NaN)
    df[col] = df[col].fillna(median_val)

# Fill categorical / object columns with mode
cat_cols = df.select_dtypes(include=["category", "object"]).columns
for col in cat_cols:
    if df[col].isnull().any():
        mode_val = df[col].mode(dropna=True)
        fill_val = mode_val[0] if len(mode_val) > 0 else ""   # safe fallback
        df[col] = df[col].fillna(fill_val)

# ---------------------------
# 6. Verify everything is filled
# ---------------------------
total_missing = int(df.isnull().sum().sum())
print("Total missing values after filling:", total_missing)
print()

# ---------------------------
# 7. Optional summary statistics (quick look)
# ---------------------------
print("Numeric summary:")
print(df.describe(include=[np.number]).T)   # descriptive stats for numeric columns
print()
print("Categorical summary (counts for each categorical column):")
for col in cat_cols:
    print(f"\nColumn: {col}")
    print(df[col].value_counts(dropna=False).head(10))  # top values (_
