import pandas as pd

# Load your dataset
df = pd.read_csv("House Data.csv")

# -----------------------------
# Identify categorical & numeric columns
# -----------------------------
categorical_cols = df.select_dtypes(include=['object']).columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("Categorical Columns:", list(categorical_cols))
print("Numeric Columns:", list(numeric_cols))

# -----------------------------
# Example: Group numeric variables by a chosen categorical variable
# -----------------------------
# You can change this to any categorical column you prefer
categorical_var = categorical_cols[0]   # first categorical column automatically

print(f"\nUsing categorical variable for grouping: {categorical_var}\n")

# Compute summary statistics for all numeric columns grouped by the categorical variable
summary = df.groupby(categorical_var)[numeric_cols].agg(
    ['mean', 'median', 'min', 'max', 'std']
)

print("=== SUMMARY STATISTICS GROUPED BY", categorical_var, "===")
print(summary)
