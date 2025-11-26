# 11. Use Iris flower dataset and perform following :
# 1. List down the features and their types (e.g., numeric, nominal)
# available in the dataset. 2. Create a histogram for each feature in the
# dataset to illustrate the feature distributions.



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 1) List features and their types
print("=== Features and Types ===")
for col in df.columns:
    print(f"{col}  -->  {df[col].dtype}")

# 2) Create histogram for each feature
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()
