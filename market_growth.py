import pandas as pd
import numpy as np

# Simulate market size data over 10 years
np.random.seed(42)
years = pd.date_range(start="2013", periods=10, freq="Y")
market_size = [100 + 10 * i + np.random.uniform(-5, 5) for i in range(10)]

data = pd.DataFrame({"Year": years, "Market_Size": market_size})
print(data)

# Calculate annual growth rate
data['Growth_Rate'] = data['Market_Size'].pct_change() * 100
print(data)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Market_Size'], marker='o', label='Market Size')
plt.title('Market Size Over Time')
plt.xlabel('Year')
plt.ylabel('Market Size')
plt.grid(True)
plt.legend()
plt.show()

from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Fit an exponential smoothing model
model = ExponentialSmoothing(data['Market_Size'], trend="add", seasonal=None)
fit = model.fit()

# Predict the next 5 years
future_years = pd.date_range(start="2023", periods=5, freq="YE")
forecast = fit.forecast(steps=5)

# Combine historical and forecast data
forecast_data = pd.DataFrame({"Year": future_years, "Market_Size": forecast})
combined_data = pd.concat([data, forecast_data], ignore_index=True)

# Visualize forecast
plt.figure(figsize=(10, 6))
plt.plot(combined_data['Year'], combined_data['Market_Size'], marker='o', label='Market Size')
plt.axvline(x=pd.Timestamp("2022"), color='gray', linestyle='--', label='Forecast Start')
plt.title('Market Growth Forecast')
plt.xlabel('Year')
plt.ylabel('Market Size')
plt.legend()
plt.grid(True)
plt.show()

#CAGR (Compound Annual Growth Rate)
start_value = data['Market_Size'].iloc[0]
end_value = data['Market_Size'].iloc[-1]
n_years = len(data) - 1
cagr = ((end_value / start_value) ** (1 / n_years) - 1) * 100
print(f"Compound Annual Growth Rate (CAGR): {cagr:.2f}%")



