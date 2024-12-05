import pandas as pd

# Load refined data from step3
file_path = 'step3_refine.csv'
pokemon_data = pd.read_csv(file_path)

# Check for missing values in the relevant columns
missing_data = pokemon_data.isnull().sum()
print("Missing Data:\n", missing_data)

# Validate ranges for numeric columns
# Ensure these columns are available from step3, and check their ranges
numeric_cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
for col in numeric_cols:
    print(f"{col}: Min = {pokemon_data[col].min()}, Max = {pokemon_data[col].max()}")

# Optionally, you can add logic to handle missing values (e.g., filling or removing rows)
# For now, we'll assume no changes to the dataset if no missing data is found

# Save cleaned data to step4_cleaned.csv
pokemon_data.to_csv('step4_cleaned.csv', index=False)
print("Step 4 completed: Cleaned data saved to 'step4_cleaned.csv'.")
