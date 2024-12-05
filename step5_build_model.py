import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Load cleaned data
file_path = 'step4_cleaned.csv'
pokemon_data = pd.read_csv(file_path)

# Ensure the column names are correct
print(pokemon_data.columns)

# Define the features and target
X = pokemon_data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]  # Features (Base stats)
y = np.random.choice([0, 1], size=pokemon_data.shape[0])  # Simulated outcome (win/lose)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'pokemon_battle_model.pkl')
print("Model trained and saved as 'pokemon_battle_model.pkl'")
