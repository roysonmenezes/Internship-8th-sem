# Assignment (07/03/2026)
# Assignment Name: KNN in Real Life
# Description: Explain Netflix-like recommendations using KNN and create a small similarity example

import numpy as np
from sklearn.neighbors import NearestNeighbors

# Sample dataset: Users and ratings for movies
# Columns represent ratings for Movie1, Movie2, Movie3
data = np.array([
    [5, 3, 4],  # User A
    [4, 2, 5],  # User B
    [1, 5, 2],  # User C
    [5, 4, 4],  # User D
])

# Fit KNN model
model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(data)

# Example: Find users similar to User A
distances, indices = model.kneighbors([data[0]])

print("Similar users to User A:")
print(indices)
print("Distances:")
print(distances)

print("\nRecommendation Insight:")
print("Users with similar ratings can be recommended similar movies.")