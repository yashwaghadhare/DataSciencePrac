# Importing libraries for data handling and visualization
import pandas as pd
import plotly.express as px
from google.colab import output
output.enable_custom_widget_manager()

# Creating a small HR dataset with department metrics
data = {
  "Department": ["HR", "Finance", "IT", "Marketing", "Operations"],
  "Headcount": [12, 18, 35, 22, 40],
  "New_Hires": [2, 1, 4, 3, 5],
  "Exits": [1, 1, 2, 1, 3],
  "Training_Hours": [120, 90, 160, 140, 180]
}

df = pd.DataFrame(data)

df

# Bar chart showing workforce size across departments
fig = px.bar(
    df, 
    x="Department", 
    y="Headcount", 
    title="Headcount by Department",
    text="Headcount"
)

fig.show()

# Line chart showing number of new hires in each department
fig = px.line(df, x="Department", y="New_Hires", 
              markers=True,
              title="Recruitment Pipeline – New Hires")
fig.show()

# Pie chart showing training hours distribution across departments
fig = px.pie(df, names="Department", values="Training_Hours",
              title="Training Hours Distribution")
fig.show()


# Calculating department exit rates as a percentage
df["Exit_Rate_%"] = round((df["Exits"] / df["Headcount"]) * 100, 2)

# Bar chart showing exit rates for each department
fig = px.bar(df, x="Department", y="Exit_Rate_%",
              title="Exit Rate (%) by Department",
              text="Exit_Rate_%")
fig.show()