import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your data into a pandas DataFrame
unfiltered_df = pd.read_csv('DRC.csv')

pre_df = unfiltered_df[unfiltered_df['confidence'].str.contains('h|n', case=False, na=False, regex=True)].reset_index(drop=True)
df = pre_df[pre_df["type"] == 0]

# Extract the "frp" and "bright_ti5" columns from the filtered DataFrame as separate DataFrames
# frp = df[["frp"]].reset_index(drop=True)
# bright_ti5 = df[["bright_ti5"]].reset_index(drop=True)

# Select features for clustering
features = df[['frp', 'bright_ti5']]

# Use the Elbow Method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)

# Choose the number of clusters (you can set it based on the elbow method)
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(features)

# Assign cluster labels to the DataFrame
df['cluster'] = kmeans.labels_

# Visualize the clusters in a scatter plot
plt.scatter(df['frp'], df['bright_ti5'], c=df['cluster'], cmap='rainbow')
plt.xlabel('frp')
plt.ylabel('bright_ti5')
plt.title("K-Means Scatter Plot of FRP vs Brightness of Vegitation Fires")
plt.show()
plt.savefig("frp_bright_ti5_kmeans.png")