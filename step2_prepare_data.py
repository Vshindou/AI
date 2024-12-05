import pandas as pd

# Load raw Pokémon data
pokemon_data = pd.read_csv("step1_organized.csv")  # Adjust the filename if necessary

# Display the original column names for verification
print("Original columns in the dataset:", pokemon_data.columns)

# Map actual column names to expected features
columns_to_keep = {
    'Pokemon': 'Pokemon',
    'Type': 'Type',  # Assuming a single 'Type' column exists
    'HP': 'HP Base',
    'Attack': 'Attack Base',
    'Defense': 'Defense Base',
    'Sp. Atk': 'Special Attack Base',
    'Sp. Def': 'Special Defense Base',
    'Speed': 'Speed Base'
}

# Extract and rename the relevant columns
cleaned_data = pokemon_data[list(columns_to_keep.values())]
cleaned_data.rename(columns={v: k for k, v in columns_to_keep.items()}, inplace=True)

# Handle missing values by filling or dropping them
cleaned_data = cleaned_data.fillna('None')  # Replace NaN with 'None'

# Save the refined Pokémon data
cleaned_data.to_csv("step2_prepare.csv", index=False)

print("Data preparation completed. Refined data saved to 'refined_pokemon_data.csv'.")
