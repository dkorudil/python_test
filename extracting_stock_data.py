import yfinance as yf
import pandas as pd
import requests
import matplotlib.pyplot as plt


#Creating ticker object for the company
apple=yf.Ticker("AAPL")

# URL of the file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"

# Send an HTTP GET request to fetch the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a file
    with open("apple.json", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
    
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
print(apple_info['country'])

#Max period apple share price data
apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())


# Reset the index of DataFrame
apple_share_price_data.reset_index(inplace=True)

# Create the first plot (apple share price)
plt.figure()
apple_share_price_data.plot(x="Date", y="Open")
plt.title("Apple Share Price")
plt.draw()  # Draw the plot without blocking execution

# Extracting Dividends and creating the second plot
plt.figure()
apple.dividends.plot()
plt.title("Apple Dividends")
plt.show()  # Now show the second plot
