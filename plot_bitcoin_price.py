import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('bitcoin_price_data.csv')

# Print the first few rows and column names to verify
print("First few rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())

# Convert the 'DateTime' column to datetime
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Plot the price trend
plt.figure(figsize=(10, 6))
plt.plot(df['DateTime'], df['Price'], marker='o', linestyle='-', color='b')
plt.title('Bitcoin Price Trend')
plt.xlabel('Date and Time')
plt.ylabel('Price in USD')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust the layout to fit labels

# Save the plot as an image file
plt.savefig('bitcoin_price_trend.png')

# Show the plot
plt.show()
