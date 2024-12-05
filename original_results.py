import pandas as pd
import matplotlib.pyplot as plt

# Load original data (pokemonDB.csv)
pokemon_data = pd.read_csv('pokemonDB.csv')

# Function to calculate battle outcome based purely on base stats (no model)
def base_stat_battle(pokemon1, pokemon2):
    stats1 = pokemon1[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
    stats2 = pokemon2[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
    
    # Compare base stats (simplified approach: sum of all stats)
    score1 = stats1.sum(axis=1).values[0]
    score2 = stats2.sum(axis=1).values[0]
    
    if score1 > score2:
        return 1  # Pokemon1 wins
    elif score2 > score1:
        return 2  # Pokemon2 wins
    else:
        return 0  # Draw

# Simulate battles based on base stats for the first 100 Pokémon
original_results = []
for i in range(100):
    for j in range(i + 1, 100):
        pokemon1 = pokemon_data.iloc[i]
        pokemon2 = pokemon_data.iloc[j]
        
        result = base_stat_battle(pokemon1, pokemon2)
        original_results.append([pokemon1['Pokemon'], pokemon2['Pokemon'], result])

# Save base stat comparison results to CSV
original_results_df = pd.DataFrame(original_results, columns=['Pokemon1', 'Pokemon2', 'Winner'])
original_results_df.to_csv('original_results.csv', index=False)
print("Base stat results saved to 'original_results.csv'")

# Plot comparison results
original_outcome_counts = original_results_df['Winner'].value_counts()
results_df = pd.read_csv('results.csv')
outcome_counts_model = results_df['Winner'].value_counts()

plt.figure(figsize=(12, 6))

# Plot original results (base stat comparison)
plt.subplot(1, 2, 1)
plt.bar(original_outcome_counts.index, original_outcome_counts.values, color='blue')
plt.title('Base Stat Battle Results')
plt.xticks([0, 1, 2], ['Draw', 'Pokemon1 Wins', 'Pokemon2 Wins'])
plt.ylabel('Count')

# Plot model results
plt.subplot(1, 2, 2)
plt.bar(outcome_counts_model.index, outcome_counts_model.values, color='orange')
plt.title('Model Battle Results')
plt.xticks([0, 1, 2], ['Draw', 'Pokemon1 Wins', 'Pokemon2 Wins'])
plt.ylabel('Count')

plt.tight_layout()
plt.show()
