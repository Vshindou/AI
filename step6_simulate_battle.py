import pandas as pd
import joblib
import random
import numpy as np

# Load the model
model = joblib.load('pokemon_battle_model.pkl')

# Load the Pokémon data
pokemon_data = pd.read_csv('step4_cleaned.csv')

# Function to predict battle outcome using the model
def predict_battle(pokemon1, pokemon2):
    # Get the base stats for the Pokémon
    stats1 = pokemon1[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].values.reshape(1, -1)
    stats2 = pokemon2[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].values.reshape(1, -1)

    # Ensure that feature names are included for prediction
    stats1_df = pd.DataFrame(stats1, columns=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
    stats2_df = pd.DataFrame(stats2, columns=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])

    # Use the model to predict battle outcome (1: win, 0: lose)
    prob1 = model.predict_proba(stats1_df)[0, 1]
    prob2 = model.predict_proba(stats2_df)[0, 1]

    # Determine the winner based on prediction probabilities
    if prob1 > prob2:
        return 1  # Pokemon1 wins
    elif prob2 > prob1:
        return 2  # Pokemon2 wins
    else:
        return 0  # Draw

# Simulate battles for the first 100 Pokémon
results = []
for i in range(10):
    for j in range(i + 1, 100):  # Battle each Pokémon against each other
        pokemon1 = pokemon_data.iloc[i]
        pokemon2 = pokemon_data.iloc[j]
        
        result = predict_battle(pokemon1, pokemon2)
        results.append([pokemon1['Pokemon'], pokemon2['Pokemon'], result])

# Save battle results to CSV
results_df = pd.DataFrame(results, columns=['Pokemon1', 'Pokemon2', 'Winner'])
results_df.to_csv('results.csv', index=False)
print("Battle results saved to 'results.csv'")

# Plot the results (optional)
import matplotlib.pyplot as plt

# Plot the battle outcomes (1 = Pokemon1 wins, 2 = Pokemon2 wins, 0 = Draw)
outcome_counts = results_df['Winner'].value_counts()

plt.bar(outcome_counts.index, outcome_counts.values)
plt.xlabel('Battle Outcome')
plt.ylabel('Count')
plt.title('Battle Results (First 100 Pokémon)')
plt.xticks([0, 1, 2], ['Draw', 'Pokemon1 Wins', 'Pokemon2 Wins'])
plt.show()
