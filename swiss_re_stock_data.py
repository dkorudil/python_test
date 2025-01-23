import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json

# Creating ticker object for Swiss Re
swiss_re = yf.Ticker("SREN.SW")

# Max period Swiss RE share price data
swiss_re_share_price_data = swiss_re.history(period="max")
print(swiss_re_share_price_data.head())

# Save data to a JSON file
swiss_re_share_price_data_json = swiss_re_share_price_data.to_json()
with open("swiss_re_share_price_data.json", "w") as file:
    file.write(swiss_re_share_price_data_json)
print("Swiss Re share price data saved to swiss_re_share_price_data.json")

# Reset the index of DataFrame
swiss_re_share_price_data.reset_index(inplace=True)

# Create the first plot (Swiss RE share price)
plt.figure()
swiss_re_share_price_data.plot(x="Date", y="Open")
plt.title("Swiss RE Share Price")
plt.draw()  # Draw the plot without blocking execution

# Extracting Dividends and creating the second plot
plt.figure()
swiss_re.dividends.plot()
plt.title("Swiss RE Dividends")
plt.show()  # Now show the second plot
