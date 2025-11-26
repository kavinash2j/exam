import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Load dataset (file should be in same folder)
df = pd.read_csv("Lipstick.csv")

# 2. Prepare features and target
df = df.drop(columns=["Id"])       # drop Id if present
X = df.drop(columns=["Buys"])
y = df["Buys"]

# 3. One-hot encode categorical variables
X_enc = pd.get_dummies(X, drop_first=False)

# 4. Train Decision Tree
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_enc, y)

# 5. Create test record exactly as asked
test = pd.DataFrame([{
    "Age": ">35",
    "Income": "Medium",
    "Gender": "Female",
    "Ms": "Married"
}])

# 6. Encode test record and align columns with training features
test_enc = pd.get_dummies(test, drop_first=False)
test_aligned = test_enc.reindex(columns=X_enc.columns, fill_value=0)

# 7. Predict
pred = clf.predict(test_aligned)[0]
probs = clf.predict_proba(test_aligned)[0]

# 8. Output
print("Test record:", test.to_dict(orient="records")[0])
print("Predicted decision (Buys):", pred)
print("Class probabilities:", dict(zip(clf.classes_, probs)))
