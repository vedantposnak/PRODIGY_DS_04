import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"D:\task4\Social_Media_Sentiment_Analysis_AI_Trends_2026-selected-columns.csv")
from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['post_text'].apply(get_sentiment)
sentiment_count = df['Sentiment'].value_counts()
print(sentiment_count)

# Bar Chart For Sentiment Analysis
sentiment_count.plot(kind='bar')
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()