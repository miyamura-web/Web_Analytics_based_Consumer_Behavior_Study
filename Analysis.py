import pandas as pd
fp = r"D:\9. Self Projects\Consumer Behaviour\Sentiment Analysis Dataset.csv"
df = pd.read_csv(fp)
df.head()

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tabulate import tabulate

analyzer = SentimentIntensityAnalyzer()

# Collect rows for the table
rows = []

# Loop through DataFrame
for idx, row in df.iterrows():
    text = row['review_text']
    date = row['purchase_date']
    name = row['product_name']

    score = analyzer.polarity_scores(text)
    
    # Add row
    rows.append([date, name, score['neg'], score['neu'], score['pos'], score['compound']])

# Define headers
headers = ["Date", "Product", "Negative", "Neutral", "Positive", "Compound"]

# Print nicely formatted table
print(tabulate(rows, headers=headers, tablefmt="grid"))