import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
csv_file = "your_file.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file)

# Extract the "frp" and "brightness" columns
frp = df["frp"]
brightness = df["brightness"]

# Create a scatter plot to visualize the data
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
plt.scatter(frp, brightness, s=20, alpha=0.5, c='blue', label="Data Points")
plt.title("Scatter Plot of FRP vs Brightness")
plt.xlabel("FRP")
plt.ylabel("Brightness")
plt.legend()
plt.grid(True)

# Display the plot or save it to a file
plt.show()  # To display the plot in a Jupyter Notebook or script
# or use plt.savefig("scatter_plot.png") to save the plot to a file

