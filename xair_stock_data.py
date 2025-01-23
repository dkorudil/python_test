import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json

# Creating ticker object for Airbus
airbus = yf.Ticker("AIR.PA")

# Max period Airbus share price data
airbus_share_price_data = airbus.history(period="max")
print(airbus_share_price_data.head())

# Save data to a JSON file
airbus_share_price_data_json = airbus_share_price_data.to_json()
with open("airbus_share_price_data.json", "w") as file:
    file.write(airbus_share_price_data_json)
print("Airbus share price data saved to airbus_share_price_data.json")

# Reset the index of DataFrame
airbus_share_price_data.reset_index(inplace=True)

# Create the first plot (Airbus share price)
plt.figure()
airbus_share_price_data.plot(x="Date", y="Open")
plt.title("Airbus Share Price")
plt.draw()  # Draw the plot without blocking execution

# Extracting Dividends and creating the second plot
plt.figure()
airbus.dividends.plot()
plt.title("Airbus Dividends")
plt.show()  # Now show the second plot
