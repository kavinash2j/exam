# 12.Use Iris flower dataset and perform following :
# 1. Create a box plot for each feature in the dataset.
# 2. Identify and discuss distributions and identify outliers from them


import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("IRIS.csv")

# 1. BOX PLOTS FOR EACH FEATURE
plt.figure(figsize=(12, 8))

features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for i, col in enumerate(features):
    plt.subplot(2, 2, i+1)
    plt.boxplot(df[col])
    plt.title(col)

plt.tight_layout()
plt.show()

# 2. IDENTIFY OUTLIERS (IQR METHOD)
print("\n=== OUTLIERS DETECTION USING IQR METHOD ===")
for col in features:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)][col]

    print(f"\n{col} → Outliers: {list(outliers.values)}")
