import pandas as pd

# Load the data
pokemon_data = pd.read_csv("step2_prepare.csv")

# Ensure the correct column names
print("Columns in the dataset:", pokemon_data.columns)

# Verify structure: Keep individual Pokémon details intact
# Optional: If you really want aggregation, modify as needed
aggregated_data = pokemon_data[['Pokemon', 'Type', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]

# Save the data without unnecessary aggregation
aggregated_data.to_csv("step3_refine.csv", index=False)

print("Refined data saved to 'refined_pokemon_data.csv'")
