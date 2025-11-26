import pandas as pd

# Read data from CSV and Excel
df_csv = pd.read_csv("Titanic.csv")
# df_xls = pd.read_excel("Titanic.xlsx")

# Use df_csv for demonstrations
df = df_csv

# Show shape and columns
print("Shape:", df.shape)
print("Columns:", list(df.columns))

# Check data types
print("\nData types:")
print(df.dtypes)

# Describe attributes
print("\nDescribe (numeric):")
print(df.describe())

print("\nDescribe (all):")
print(df.describe(include="all"))

# Missing values per column
print("\nMissing values:")
print(df.isnull().sum())

# Indexing & selecting (iloc examples)
print("\niloc - first row:")
print(df.iloc[0])

print("\niloc - first 5 rows:")
print(df.iloc[0:5])

print("\niloc - first 5 rows, first 3 columns:")
print(df.iloc[0:5, 0:3])

print("\niloc - single cell (row 2, col 3):")
print(df.iloc[2, 3])

# Indexing & selecting (loc examples)
print("\nloc - rows 0 to 4:")
print(df.loc[0:4])

print("\nloc - rows 0 to 4, columns Name, Age, Sex:")
print(df.loc[0:4, ["Name", "Age", "Sex"]])

print("\nloc - single cell (row 0, 'Age'):")
print(df.loc[0, "Age"])

# Single-column selection
print("\nSingle column 'Age' (first 5):")
print(df["Age"].head())

# Multiple-column selection
print("\nMultiple columns (Name, Age, Sex) (first 5):")
print(df[["Name", "Age", "Sex"]].head())

# Boolean indexing example (survivors)
print("\nBoolean indexing - survivors (Survived == 1) (first 5):")
print(df[df["Survived"] == 1].head())

# Sorting - single column
print("\nSort by Age ascending (first 5):")
print(df.sort_values(by="Age", ascending=True).head())

print("\nSort by Age descending (first 5):")
print(df.sort_values(by="Age", ascending=False).head())

# Sorting - multiple columns
print("\nSort by Pclass ASC, Age ASC (first 5):")
print(df.sort_values(by=["Pclass", "Age"], ascending=[True, True]).head())

print("\nSort by Pclass ASC, Age DESC (first 5):")
print(df.sort_values(by=["Pclass", "Age"], ascending=[True, False]).head())

print("\nSort by Fare DESC, Age DESC (first 5):")
print(df.sort_values(by=["Fare", "Age"], ascending=[False, False]).head())

# Sort index
print("\nSort by index (first 5):")
print(df.sort_index().head())
