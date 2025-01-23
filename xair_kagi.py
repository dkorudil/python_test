import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Create ticker object for Airbus
airbus = yf.Ticker("AIR.PA")
airbus_share_price_data = airbus.history(period="max")

# Reset the index and prepare data
airbus_share_price_data.reset_index(inplace=True)

# Create a Kagi chart using Plotly
fig = go.Figure(
    data=go.Candlestick(
        x=airbus_share_price_data['Date'],
        open=airbus_share_price_data['Open'],
        high=airbus_share_price_data['High'],
        low=airbus_share_price_data['Low'],
        close=airbus_share_price_data['Close']
    )
)

fig.update_layout(
    title="Airbus Kagi Chart",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_dark"
)

fig.show()
