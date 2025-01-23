import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json

# Creating ticker object for Crocs
crocs = yf.Ticker("CRKN")

# Max period Crocs share price data
crocs_share_price_data = crocs.history(period="max")
print(crocs_share_price_data.head())

# Save data to a JSON file
crocs_share_price_data_json = crocs_share_price_data.to_json()
with open("crocs_share_price_data.json", "w") as file:
    file.write(crocs_share_price_data_json)
print("Crocs share price data saved to crocs_share_price_data.json")

# Reset the index of DataFrame
crocs_share_price_data.reset_index(inplace=True)

# Create the first plot (Crocs share price)
plt.figure()
crocs_share_price_data.plot(x="Date", y="Open")
plt.title("Crocs Share Price")
plt.draw()  # Draw the plot without blocking execution

# Extracting Dividends and creating the second plot
plt.figure()
crocs.dividends.plot()
plt.title("Crocs Dividends")
plt.show()  # Now show the second plot
