# Compute Accuracy, Error rate, Precision, Recall for the following
# confusion matrix.
# Actual Class\Predicted
# class
# cancer =
# yes
# cancer = no Total
# cancer = yes 90 210 300
# cancer = no 140 9560 9700
# Total 230 9770 10000


TP = 90
FN = 210
FP = 140
TN = 9560

# Accuracy
accuracy = (TP + TN) / (TP + TN + FP + FN)

# Error Rate
error_rate = (FP + FN) / (TP + TN + FP + FN)

# Precision
precision = TP / (TP + FP)

# Recall
recall = TP / (TP + FN)

print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)
