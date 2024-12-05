import pandas as pd

# Step 1: Load and organize data
file_path = 'pokemonDB.csv'  # Replace with your dataset file path
pokemon_data = pd.read_csv(file_path)

# Validate and save organized data
pokemon_data.to_csv('step1_organized.csv', index=False)
print("Step 1 completed: Organized data saved to 'step1_organized.csv'.")
