# 17. Compute Accuracy, Error rate, Precision, Recall for following confusion
# matrix ( Use formula for each)
# True Positives (TPs): 1 False Positives (FPs): 1
# False Negatives (FNs): 8 True Negatives (TNs): 90


# Given values
TP = 1
FP = 1
FN = 8
TN = 90

# Calculations
accuracy = (TP + TN) / (TP + TN + FP + FN)
error_rate = (FP + FN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)

# Print results
print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)
