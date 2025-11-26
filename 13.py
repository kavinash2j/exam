# 13. Use the covid_vaccine_statewise.csv dataset and perform the following
# analytics.
# a. Describe the dataset
# b. Number of persons state wise vaccinated for first dose in India
# c. Number of persons state wise vaccinated for second dose in India



import pandas as pd

# Load dataset
df = pd.read_csv("Covid Vaccine Statewise.csv")

# -----------------------------
# a) Describe the dataset
# -----------------------------
print("=== Dataset Info ===")
df.info()

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Statistical Description (Numeric Columns) ===")
print(df.describe())

print("\n=== Statistical Description (All Columns) ===")
print(df.describe(include='all'))

# -----------------------------
# b) State-wise First Dose Vaccination
# -----------------------------
first_dose = df.groupby("State")["First Dose Administered"].sum()

print("\n=== Total First Dose Administered State-wise ===")
print(first_dose)

# -----------------------------
# c) State-wise Second Dose Vaccination
# -----------------------------
second_dose = df.groupby("State")["Second Dose Administered"].sum()

print("\n=== Total Second Dose Administered State-wise ===")
print(second_dose)
