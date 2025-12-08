import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Employee_ID': [101,102,103,104,105],
    'Department': ['HR','IT','IT','Finance','HR'],
    'Training_Module':    
    ['Excel','Python','Python','Excel','Communication'],
    'Pre_Score': [45, 50, 30, 55, 40],
    'Post_Score': [70, 85, 55, 80, 60],
}

df = pd.DataFrame(data)
df

df['Improvement'] = df['Post_Score'] - df['Pre_Score']
df

avg_pre = df['Pre_Score'].mean()
avg_post = df['Post_Score'].mean()
avg_improvement = df['Improvement'].mean()

print("Average Pre-Training Score :", avg_pre)
print("Average Post-Training Score:", avg_post)
print("Average Improvement        :", avg_improvement)

# Rule: if Post Score < 60 → skill gap exists
df['Skill_Gap'] = df['Post_Score'] < 60
df

module_improvement = df.groupby('Training_Module')['Improvement'].mean()

plt.figure(figsize=(6,4))
module_improvement.plot(kind='bar')
plt.title("Average Improvement by Training Module")
plt.xlabel("Training Module")
plt.ylabel("Improvement Score")
plt.show()