# Assignment (03/03/2026)
# Assignment Name: Build Your First Dataset
# Description: Create a dataset (study hours vs marks), identify features & labels, predict relationship

import pandas as pd

# Creating dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Identifying feature and label
X = df["Study_Hours"]   # Feature
y = df["Marks"]         # Label

print("\nFeature (Input): Study Hours")
print(X)

print("\nLabel (Output): Marks")
print(y)

# Simple prediction relationship
print("\nPrediction Insight:")
print("As study hours increase, marks also increase. This shows a positive relationship.")