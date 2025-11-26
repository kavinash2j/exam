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
