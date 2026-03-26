# Assignment (18/03/2026)
# Assignment Name: Customer Segmentation
# Description: Perform K-Means clustering on a mall dataset and describe customer groups

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Extended dataset (more variation)
data = {
    "Annual_Income": [20, 25, 30, 35, 40, 60, 65, 70, 75, 80],
    "Spending_Score": [30, 35, 40, 45, 50, 60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(df)

print("Clustered Customer Data:")
print(df)

# Visualize clusters
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation (3 Clusters)")
plt.show()