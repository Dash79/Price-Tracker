import requests
import time
import csv
from datetime import datetime

# URL of the CoinGecko API for Bitcoin price
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Function to fetch and log the Bitcoin price
def track_bitcoin_price():
    with open('bitcoin_price_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header only if the file is new/empty
        file.seek(0, 2)  # Move the cursor to the end of the file
        if file.tell() == 0:
            writer.writerow(['DateTime', 'Price'])

        while True:
            try:
                # Send a GET request to the API
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad status codes
                data = response.json()

                # Extract the current Bitcoin price in USD
                bitcoin_price = data['bitcoin']['usd']

                # Get the current date and time
                date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Print the extracted information
                print(f"Bitcoin Price: ${bitcoin_price}")
                print(f"Date and Time: {date_time}")
                print("-" * 40)  # Just a separator for readability

                # Write the data to the CSV file
                writer.writerow([date_time, bitcoin_price])

            except requests.RequestException as e:
                print(f"Error fetching data: {e}")

            # Wait for 1 hour before fetching the price again
            time.sleep(3600)  # 3600 seconds = 1 hour

# Start tracking the Bitcoin price
track_bitcoin_price()
