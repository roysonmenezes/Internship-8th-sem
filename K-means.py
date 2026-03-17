# Assignment (11/03/2026)
# Assignment Name: Customer Segmentation
# Description: Perform K-Means clustering on a mall dataset and describe customer groups

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset (Annual Income vs Spending Score)
data = {
    "Annual_Income": [15, 16, 17, 18, 19, 60, 62, 65, 70, 72],
    "Spending_Score": [39, 81, 6, 77, 40, 55, 52, 59, 60, 54]
}

df = pd.DataFrame(data)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=0)
df["Cluster"] = kmeans.fit_predict(df)

print(df)

# Plot clusters
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()