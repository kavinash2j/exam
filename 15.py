import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("Titanic.csv")

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Dataset Info ===")
print(df.info())

# ------------------------------
# 1. Age Distribution
# ------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution of Titanic Passengers")
plt.show()

# ------------------------------
# 2. Survival Count by Gender
# ------------------------------
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival Count by Gender")
plt.show()

# ------------------------------
# 3. Survival Rate by Passenger Class
# ------------------------------
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.show()

# ------------------------------
# 4. Correlation Heatmap
# ------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------
# 5. Fare vs Age Scatter Plot
# ------------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived")
plt.title("Age vs Fare with Survival Status")
plt.show()

# ------------------------------
# 6. Gender-wise Age Distribution by Survival
# ------------------------------
g = sns.FacetGrid(df, col="Survived", row="Sex", height=3)
g.map_dataframe(sns.histplot, x="Age", bins=20)
plt.show()
