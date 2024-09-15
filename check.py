import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('bitcoin_price_data.csv')

# Print the column names to verify
print("Columns in CSV file:", df.columns.tolist())
