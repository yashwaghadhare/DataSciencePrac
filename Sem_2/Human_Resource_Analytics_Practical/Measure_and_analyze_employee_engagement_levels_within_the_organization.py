import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": ["E1", "E2", "E3", "E4", "E5"],
    "Job_Satisfaction": [4, 5, 3, 4, 2],
    "Work_Environment": [5, 4, 4, 3, 2],
    "Culture": [4, 5, 3, 4, 3]
}

df = pd.DataFrame(data)
display(df)

df["Engagement_Score"] = df[["Job_Satisfaction", "Work_Environment", "Culture"]].mean(axis=1)
display(df)

plt.figure(figsize=(6, 4))
plt.plot(df["Employee"], df["Engagement_Score"], marker="o")
plt.xlabel("Employee")
plt.ylabel("Engagement Score")
plt.title("Employee Engagement Levels")
plt.grid()
plt.show()

feedback_data = {
    "Employee": ["E1", "E2", "E3", "E4", "E5"],
    "Feedback": [
        "The work environment is great and supportive.",
        "I love the culture and overall experience.",
        "Some processes are confusing and need improvement.",
        "Good team but workload is high sometimes.",
        "Not satisfied with the work environment."
    ]
}

feedback_df = pd.DataFrame(feedback_data)
display(feedback_df)

positive_words = ["good", "great", "love", "supportive"]
negative_words = ["not", "bad", "confusing", "high"]

def simple_sentiment(text):
    text = text.lower()
    score = 0
    for w in positive_words:
        if w in text:
            score += 1
    for w in negative_words:
        if w in text:
            score -= 1
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

feedback_df["Sentiment"] = feedback_df["Feedback"].apply(simple_sentiment)
display(feedback_df)

sent_counts = feedback_df["Sentiment"].value_counts()

plt.figure(figsize=(5, 4))
plt.bar(sent_counts.index, sent_counts.values)
plt.title("Sentiment Count")
plt.xlabel("Sentiment")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.show()