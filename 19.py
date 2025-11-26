# Write a Python program to display some basic statistical details like
# percentile, mean, standard deviation etc (Use python and pandas
# commands) the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’
# of iris.csv dataset.


import pandas as pd

# Load iris dataset
df = pd.read_csv("iris.csv")

# List of species to analyze
species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

for species in species_list:
    print(f"\n=== Statistical Summary for {species} ===")
    
    # Filter species
    df_species = df[df['species'] == species]
    
    # Basic statistics
    print(df_species.describe())
    
    # Additional statistics
    print("\nPercentiles:")
    print(df_species.select_dtypes(include='number').quantile([0.25, 0.50, 0.75]))
    
    print("\nMean values:")
    print(df_species.mean(numeric_only=True))
    
    print("\nStandard deviation:")
    print(df_species.std(numeric_only=True))
    
    print("-" * 60)
