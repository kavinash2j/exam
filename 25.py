# Titanic: Data Cleaning & Transformation (ready-to-run)
# - Loads "Titanic.csv" from current folder
# - Performs typical cleaning steps and feature engineering
# - Encodes categorical variables and scales selected numeric features
# - Saves cleaned dataframe to "Titanic_cleaned.csv"

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("Titanic.csv")

# 2. Quick inspection
print("Initial shape:", df.shape)
print(df.info())
print(df.head(3))

# 3. Remove exact duplicate rows (if any)
df = df.drop_duplicates().reset_index(drop=True)

# 4. Basic column cleanup: strip column names
df.columns = df.columns.str.strip()

# 5. Extract useful info from existing columns
# 5.1 Extract Title from Name (Mr, Mrs, Miss, Master, Rare)
df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.', expand=False).str.strip()
# group rare titles
rare_titles = ['Dr','Rev','Col','Major','Jonkheer','Don','Dona','Lady','the Countess','Sir','Capt']
df["Title"] = df["Title"].replace(rare_titles, "Rare")
df["Title"] = df["Title"].replace({'Mlle':'Miss','Ms':'Miss','Mme':'Mrs'})

# 5.2 Extract Deck from Cabin (first letter) and mark missing as 'Unknown'
df["Deck"] = df["Cabin"].fillna("Unknown").astype(str).str[0]
df.loc[df["Deck"] == "U", "Deck"] = "Unknown"   # unify

# 5.3 Create Family size & IsAlone
df["FamilySize"] = df["SibSp"].fillna(0).astype(int) + df["Parch"].fillna(0).astype(int) + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# 6. Fill missing values
# 6.1 Fill Embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 6.2 Fill Fare with median
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# 6.3 Fill Age using median by (Title) — better than global median
age_medians = df.groupby("Title")["Age"].median()
df["Age"] = df.apply(lambda r: age_medians[r["Title"]] if pd.isnull(r["Age"]) else r["Age"], axis=1)

# 7. Drop or keep columns
# Keep: PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, Title, Deck, FamilySize, IsAlone, Survived (if present)
# Drop: unnecessary columns that are textual/duplicates for modeling (we drop Ticket and full Cabin)
df = df.drop(columns=["Ticket", "Cabin"])

# 8. Convert dtypes / encode categorical variables
# 8.1 Sex -> binary
df["Sex"] = df["Sex"].map({"male": 1, "female": 0}).astype(int)

# 8.2 Title, Embarked, Deck, Pclass -> one-hot
cat_cols = ["Title", "Embarked", "Deck", "Pclass"]
df = pd.get_dummies(df, columns=cat_cols, prefix=cat_cols, drop_first=False)

# 9. Numeric feature transformations
# 9.1 Log-transform Fare to reduce skew (add small constant)
df["Fare_log"] = np.log1p(df["Fare"])

# 9.2 Scale Age and Fare_log
scaler = StandardScaler()
df[["Age_scaled", "Fare_log_scaled"]] = scaler.fit_transform(df[["Age", "Fare_log"]])

# 10. Final checks
print("\nMissing values per column after cleaning:")
print(df.isnull().sum()[lambda x: x>0])   # show only columns with missing values

print("\nFinal dtypes:")
print(df.dtypes)

print("\nPreview cleaned data:")
print(df.head(5).T)

# 11. Save cleaned dataset
df.to_csv("Titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved to 'Titanic_cleaned.csv' (shape: {})".format(df.shape))
