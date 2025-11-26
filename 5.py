# Write a program to do: A dataset collected in a cosmetics shop showing
# details of customers and whether or not they responded to a special offer
# to buy a new lip-stick is shown in table below. (Use library commands)
# According to the decision tree you have made from the previous training
# data set, what is the decision for the test data: [Age < 21, Income = Low,
# Gender = Female, Marital Status = Married]?

# Decision tree prediction for given test instance
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# 1) Load training data (CSV file). The file must contain these columns:
#    Age, Income, Gender, MaritalStatus, Buys
df = pd.read_csv("Lipstick.csv")

# 2) Prepare features and target
X = df.drop(columns=["Buys"])
y = df["Buys"]

# 3) Convert categorical features to numeric using one-hot encoding
X_encoded = pd.get_dummies(X, drop_first=False)

# 4) Train a Decision Tree classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_encoded, y)

# 5) Create the test record exactly as requested:
#    Age < 21  -> represent as category e.g. "LessThan21" or "Young" depending on your data.
#    Income = Low
#    Gender = Female
#    Marital Status = Married
#
# Adjust the Age value below to match the categorical values used in your CSV.
test_record = pd.DataFrame([{
    "Age": "<21",            # change to exact level used in your CSV (e.g. "Young" or "<21")
    "Income": "Low",
    "Gender": "Female",
    "MaritalStatus": "Married"
}])

# 6) One-hot encode the test record and align columns with training features
test_encoded = pd.get_dummies(test_record, drop_first=False)
test_aligned = test_encoded.reindex(columns=X_encoded.columns, fill_value=0)

# 7) Predict and show probabilities
pred = clf.predict(test_aligned)[0]
probs = clf.predict_proba(test_aligned)[0]

# 8) Print results
print("Test record:", test_record.to_dict(orient='records')[0])
print("Predicted class (Buys?):", pred)
print("Class probabilities:")
for label, p in zip(clf.classes_, probs):
    print(f"  {label}: {p:.4f}")
