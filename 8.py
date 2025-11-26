# Write a program to do: A dataset collected in a cosmetics shop showing
# details of customers and whether or not they responded to a special offer
# to buy a new lip-stick is shown in table below. (Use library commands)
# According to the decision tree you have made from the previous training
# data set, what is the decision for the test data: [Age = 21-35, Income = Low,
# Gender = Male, Marital Status = Married]?


import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("Lipstick.csv")

# Prepare features and target
df2 = df.drop(columns=["Id"])
X = df2.drop(columns=["Buys"])
y = df2["Buys"]

# One-hot encode categorical features
X_enc = pd.get_dummies(X, drop_first=False)

# Train Decision Tree
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_enc, y)

# Test instance
test = pd.DataFrame([{
    "Age": "21-35",
    "Income": "Low",
    "Gender": "Male",
    "Ms": "Married"
}])

# Encode and align test instance
test_enc = pd.get_dummies(test, drop_first=False)
test_aligned = test_enc.reindex(columns=X_enc.columns, fill_value=0)

# Predict
pred = clf.predict(test_aligned)[0]
probs = dict(zip(clf.classes_, clf.predict_proba(test_aligned)[0]))

print("Predicted decision (Buys):", pred)
print("Class probabilities:", probs)
