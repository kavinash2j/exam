#  Perform Data Cleaning, Data transformation using Python on any data
# set.

# Titanic: Data Cleaning & Transformation (ready-to-run)
# - Loads "Titanic.csv" from current folder
# - Performs typical cleaning steps and feature engineering
# - Encodes categorical variables and scales selected numeric features
# - Saves cleaned dataframe to "Titanic_cleaned.csv"

# ----------------------------------------------------------
#  IMPORT LIBRARIES
# ----------------------------------------------------------
import pandas as pd               # For loading & cleaning data
import numpy as np                # For math functions (log)
from sklearn.preprocessing import StandardScaler  # For scaling numbers


# ----------------------------------------------------------
# 1. LOAD DATASET
# ----------------------------------------------------------
df = pd.read_csv("Titanic.csv")   # Load Titanic dataset from file
print("Initial shape:", df.shape) # Print starting rows & columns


# ----------------------------------------------------------
# 2. BASIC CLEANING
# ----------------------------------------------------------
df = df.drop_duplicates()         # Remove duplicate rows
df = df.reset_index(drop=True)    # Reset row numbers after removing duplicates
df.columns = df.columns.str.strip()   # Remove spaces from column names


# ----------------------------------------------------------
# 3. FEATURE CREATION (NEW COLUMNS)
# ----------------------------------------------------------

# ---- 3.1 Extract "Title" from Name (Mr, Miss, Mrs, etc.)
df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.')  # get text between comma and dot
df["Title"] = df["Title"].replace({'Mlle':'Miss','Ms':'Miss','Mme':'Mrs'})  # group same titles

# Convert rare unusual titles into "Rare"
rare_titles = ['Dr','Rev','Col','Major','Jonkheer','Don','Dona','Lady','the Countess','Sir','Capt']
df["Title"] = df["Title"].replace(rare_titles, "Rare")


# ---- 3.2 Extract Deck from Cabin (first letter)
df["Deck"] = df["Cabin"].fillna("Unknown").astype(str).str[0]  # take first letter
df.loc[df["Deck"] == "U", "Deck"] = "Unknown"                  # unify Unknown


# ---- 3.3 Create FamilySize and IsAlone
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1    # family members on board
df["IsAlone"] = (df["FamilySize"] == 1).astype(int) # 1 = alone, 0 = not alone


# ----------------------------------------------------------
# 4. FILL MISSING VALUES
# ----------------------------------------------------------

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # fill most common value
df["Fare"] = df["Fare"].fillna(df["Fare"].median())               # fill missing Fare with median

# ---- Fill Age using median age of people with similar Title
age_median = df.groupby("Title")["Age"].median()     # find median age for each title
df["Age"] = df.apply(lambda r: age_median[r["Title"]] if pd.isnull(r["Age"]) else r["Age"], axis=1)


# ----------------------------------------------------------
# 5. REMOVE UNUSED COLUMNS
# ----------------------------------------------------------
df = df.drop(columns=["Ticket", "Cabin"])   # remove non-useful text columns


# ----------------------------------------------------------
# 6. ENCODING (Convert text → numbers)
# ----------------------------------------------------------

# ---- 6.1 Convert Sex to binary (male=1, female=0)
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

# ---- 6.2 One-hot encode categorical columns
df = pd.get_dummies(df, columns=["Title", "Embarked", "Deck", "Pclass"], drop_first=False)


# ----------------------------------------------------------
# 7. NUMERIC TRANSFORMATIONS
# ----------------------------------------------------------

df["Fare_log"] = np.log1p(df["Fare"])   # log transformation to reduce skew

# Scale Age and Fare_log
scaler = StandardScaler()                
df[["Age_scaled", "Fare_log_scaled"]] = scaler.fit_transform(df[["Age", "Fare_log"]])


# ----------------------------------------------------------
# 8. FINAL CHECKS + SAVE
# ----------------------------------------------------------
print("\nMissing values after cleaning:\n", df.isnull().sum())
print("Final shape:", df.shape)

df.to_csv("Titanic_cleaned.csv", index=False)  # Save cleaned file
print("\nFile Saved: Titanic_cleaned.csv")
