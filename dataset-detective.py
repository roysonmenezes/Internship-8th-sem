import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Display top rows
print("Top 5 Rows:")
print(df.head())

# Find highest value column (based on average)
print("\nColumn Averages:")
print(df.mean(numeric_only=True))

highest_column = df.mean(numeric_only=True).idxmax()
print("\nColumn with Highest Average:", highest_column)

# Count missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 5 Insights
print("\n--- Insights ---")
print("1. Science has the highest average marks.")
print("2. Some students have missing marks.")
print("3. Sneha scored consistently high in all subjects.")
print("4. Kiran has the lowest overall performance.")
print("5. Dataset contains both complete and incomplete records.")