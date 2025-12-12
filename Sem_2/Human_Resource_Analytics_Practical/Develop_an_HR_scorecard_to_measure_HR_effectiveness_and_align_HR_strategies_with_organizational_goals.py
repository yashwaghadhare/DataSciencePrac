# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create HR dataset
data = {
    'Year': [2022, 2023, 2024],
    'Total_Employees': [100, 120, 140],
    'Employees_Left': [10, 15, 12],
    'Training_Investment': [200000, 250000, 300000],
    'Productivity_Gain': [250000, 300000, 380000],
    'Engagement_Score': [3.2, 3.6, 4.1],
}

# Convert data to DataFrame
df = pd.DataFrame(data)
df

# Calculate HR metrics
df['Turnover_Rate'] = (df['Employees_Left'] / df['Total_Employees']) * 100
df['Training_ROI'] = (df['Productivity_Gain'] - df['Training_Investment']) / df['Training_Investment']
df['Engagement_Index'] = (df['Engagement_Score'] / 5) * 100

df

# Create HR scorecard table
scorecard = df[['Year', 'Turnover_Rate', 'Training_ROI', 'Engagement_Index']]
scorecard

# Visualize Turnover Rate trend
plt.figure(figsize=(7,4))
plt.plot(df['Year'], df['Turnover_Rate'], marker='o')
plt.xlabel("Year")
plt.ylabel("Turnover Rate (%)")
plt.title("Turnover Rate Trend")
plt.grid()
plt.show()

# Visualize Training ROI trend
plt.figure(figsize=(7,4))
plt.plot(df['Year'], df['Training_ROI'], marker='o')
plt.xlabel("Year")
plt.ylabel("Training ROI")
plt.title("Training ROI Trend")
plt.grid()
plt.show()

# Visualize Engagement Index trend
plt.figure(figsize=(7,4))
plt.plot(df['Year'], df['Engagement_Index'], marker='o')
plt.xlabel("Year")
plt.ylabel("Engagement Index (%)")
plt.title("Employee Engagement Trend")
plt.grid()
plt.show()
