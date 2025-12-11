import pandas as pd

# Generate monthly dates from Jan-2020 to Dec-2022 using month-start frequency ("MS")
dates = pd.date_range(start="2020-01-01", end="2022-12-01", freq="MS")

# Manually created real-like monthly sales values for 36 months
sales = [210,220,250,300,320,330,290,270,260,240,230,220,
         215,225,255,310,325,335,295,275,265,245,235,225,
         220,230,260,315,330,340,300,280,270,250,240,230]

# Build DataFrame and extract month number for seasonal grouping
df = pd.DataFrame({"Date": dates, "Sales": sales})
df["Month"] = df["Date"].dt.month

# Compute 12-month Moving Average (MA12); this smooths trend but is not centered
df["MA12"] = df["Sales"].rolling(window=12).mean()

# Compute Centered Moving Average (CMA); needed for ratio-to-moving-average method
df['CMA'] = df['Sales'].rolling(window=12, center=True).mean()

# Compute ratio of actual sales to CMA to isolate seasonal effect
# Ratio = (Actual / CMA) × 100; early and late months will be NaN because CMA needs 12 centered values
df["Ratio"] = (df["Sales"] / df["CMA"]) * 100
df["Ratio"].head(10)

# Compute average ratio per month (Jan–Dec) to estimate seasonal pattern
monthly_ratio = df.groupby("Month")["Ratio"].mean()
monthly_ratio.head()

# Normalize seasonal indices so that their total = 1200 (i.e., average = 100)
seasonal_indices = (monthly_ratio / monthly_ratio.sum()) * 1200
seasonal_indices.head()
