import pandas as pd
import numpy as np
import plotly.express as px
from google.colab import output
output.enable_custom_widget_manager()

data = {
  "Employee_ID": range(1, 31),
  "Department": ["HR","Finance","IT","Marketing","Operations"] * 6,
  "Job_Role": ["Executive","Manager","Analyst","Assistant","Technician"] * 6,
  "Tenure_Years": np.random.randint(1, 12, 30),
  "Salary": np.random.randint(25000, 90000, 30),
  "Performance_Rating": np.random.randint(1, 6, 30),
  "Job_Satisfaction": np.random.randint(1, 6, 30),
  "Attrition": np.random.choice(["Yes", "No"], 30, p=[0.3, 0.7])
}

df = pd.DataFrame(data)

df.head()

turnover_rate = (df[df["Attrition"] == "Yes"].shape[0] / df.shape[0]) * 100
print("Overall Turnover Rate:", round(turnover_rate, 2), "%")

turnover_rate

dept_turnover = df.groupby("Department")["Attrition"].apply(
  lambda x: (x == "Yes").mean() * 100
).reset_index(name="Turnover_Rate_%")

dept_turnover

fig = px.bar(
  dept_turnover,
  x="Department",
  y="Turnover_Rate_%",
  title="Turnover Rate by Department",
  text="Turnover_Rate_%"
)
fig.show()