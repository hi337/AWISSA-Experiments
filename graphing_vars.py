import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
csv_file = "DRC.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file)

pre_filtered_df = df[df['confidence'].str.contains('h|n', case=False, na=False, regex=True)].reset_index(drop=True)
filtered_df = pre_filtered_df[pre_filtered_df['type'] == 0].reset_index(drop=True)

# Extract the "frp" and "bright_ti5" columns from the filtered DataFrame as separate DataFrames
frp = filtered_df[["frp"]]
track = filtered_df[["track"]]

# Create a scatter plot to visualize the data
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
plt.scatter(frp, track, s=20, alpha=0.5, c='blue', label="Data Points")
plt.title("Scatter Plot of FRP vs Brightness of Vegitation Fires")
plt.xlabel("FRP")
plt.ylabel("Brightness")
plt.legend()
plt.grid(True)

# Display the plot or save it to a file
plt.show()  # To display the plot in a Jupyter Notebook or script
plt.savefig("frp_vs_track.png")

