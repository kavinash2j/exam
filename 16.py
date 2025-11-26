# . Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
# contains information about the passengers who boarded the unfortunate
# Titanic ship. Write a code to check how the price of the ticket (column
# name: 'fare') for each passenger is distributed by plotting a histogram.


import seaborn as sns
import matplotlib.pyplot as plt

# Load inbuilt Titanic dataset
titanic = sns.load_dataset("titanic")

# Plot histogram for fare distribution
plt.figure(figsize=(10, 6))
sns.histplot(titanic["fare"], bins=40, kde=True)
plt.title("Distribution of Ticket Fare on Titanic")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()
