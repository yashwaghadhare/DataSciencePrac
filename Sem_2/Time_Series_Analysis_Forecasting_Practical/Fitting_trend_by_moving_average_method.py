# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create example time series data as a pandas Series
data = [100, 110, 130, 120, 140, 150]
TS = pd.Series(data)

# Compute ordinary 4-period moving average (not centered)
MA = TS.rolling(window=4).mean()

# Compute centered moving average by applying a 2-period moving average to MA
CMA = MA.rolling(window=2).mean()

# Plot original time series and centered moving average trend
plt.figure(figsize=(10,4))
plt.plot(TS, label="Original Data", marker='o')
plt.plot(CMA, label="Centered 4-Period MA Trend", linewidth=2)
plt.legend()
plt.title("Trend Fitting by Moving Average")
plt.grid(True)
plt.show()
