import pandas as pd

# Load iris dataset
df = pd.read_csv("iris.csv")   # make sure file name matches your dataset

# List of species to analyze
species_list = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

for species in species_list:
    print(f"\n=== Statistical Summary for {species} ===")
    
    # Filter species
    df_species = df[df['species'] == species]
    
    # Basic statistics using describe()
    print(df_species.describe())
    
    # Additional required statistics
    print("\nPercentiles:")
    print(df_species.quantile([0.25, 0.50, 0.75]))
    
    print("\nMean values:")
    print(df_species.mean(numeric_only=True))
    
    print("\nStandard deviation:")
    print(df_species.std(numeric_only=True))
    
    print("-" * 60)

