#  Write a program to do: A dataset collected in a cosmetics shop showing
# details of customers and whether or not they responded to a special offer
# to buy a new lip-stick is shown in table below. (Use library commands)
# According to the decision tree you have made from the previous training
# data set, what is the decision for the test data: [Age > 35, Income =
# Medium, Gender = Female, Marital Status = Married]




import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load provided dataset
df = pd.read_csv("Lipstick.csv")

# Prepare data
df2 = df.drop(columns=["Id"])
X = df2.drop(columns=["Buys"])
y = df2["Buys"]

# Encode categorical variables
X_enc = pd.get_dummies(X)

# Train Decision Tree
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_enc, y)

# Test data
test = pd.DataFrame([{
    "Age": ">35",
    "Income": "Medium",
    "Gender": "Female",
    "Ms": "Married"
}])

# Encode test row
test_enc = pd.get_dummies(test)
test_aligned = test_enc.reindex(columns=X_enc.columns, fill_value=0)

# Prediction
pred = clf.predict(test_aligned)[0]
probs = clf.predict_proba(test_aligned)[0]

print("Decision:", pred)
print("Probabilities:", probs)
