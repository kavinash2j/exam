import pandas as pd

# Load the dataset
df = pd.read_csv("Covid Vaccine Statewise.csv")

# -----------------------------
# A. Describe the dataset
# -----------------------------
print("=== DATASET INFO ===")
df.info()

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe(include='all'))

# -----------------------------
# B. Number of males vaccinated
# -----------------------------
male_total = df["Male(Individuals Vaccinated)"].sum()
print("\n=== TOTAL MALES VACCINATED IN INDIA ===")
print(int(male_total))

# -----------------------------
# C. Number of females vaccinated
# -----------------------------
female_total = df["Female(Individuals Vaccinated)"].sum()
print("\n=== TOTAL FEMALES VACCINATED IN INDIA ===")
print(int(female_total))
