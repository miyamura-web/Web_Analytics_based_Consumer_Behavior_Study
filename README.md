# Analyzing Consumer Behavior through Web Analytics (In Process)

## 📊 Project Overview :
In the era of digital commerce, understanding consumer behavior is critical for optimizing user experience and driving sales. This project focuses on analyzing consumer interactions with the Myntra e-commerce platform using Web Analytics Data combined with Sentiment Analysis on product-related consumer feedback.

## 📚 Method :
The project involves two main components:

• **Web Analytics Analysis** – Using data such as page views, session duration, traffic sources, bounce rates, and conversions to understand how different user segments (based on age groups and traffic sources) engage with the website.

• **Sentiment Analysis** – Applying natural language processing techniques on customer reviews to assess the sentiment (positive, neutral, negative) associated with different products, identifying consumer perceptions and their potential influence on purchasing behavior.

An interactive Power BI dashboard visualizes key insights, making it easy to track consumer engagement patterns, identify bottlenecks in the user journey, and highlight sentiment trends. The project helps businesses like Myntra make data-driven decisions to enhance user engagement, improve product offerings, and ultimately increase conversion rates.

---
### 🎯 Objectives 
- Analyze user behavior across different age groups.
- Study the relationship between pages visited, session duration, and conversion rates.
- Visualize traffic sources and their impact on user engagement.
- Identify high bounce rate pages and potential areas for improvement.
- Explore consumer personality patterns based on web analytics.

---
### ⚙️Tools Used :
- **Power BI** – For interactive dashboard visualization.
- **Python** – For Sentiment Analysis and also for data pre-processing and cleaning before importing into Power BI.
---

### 📁 Project Structure :

```
├── data/
│   ├── Google_analytics_data.csv
│   └── Sentiment Analysis Dataset.csv    # Dataset used
├── dashboard/
│   └── Web_Analytics_Dashboard.pbix  # Power BI Dashboard file
├── pythoon file/
│   └── Analysis.py  # Sentiment analysis using python file
├── README.md
```

### 📊 Dashboard Highlights :

- Total Pages Visited
- Average Session Duration
- Total Conversion Count
- Conversion by Age Group
- Conversion vs. Pages Visited
- Traffic Source Distribution
- Bounce Rate by Landing Page
  
<img width="1308" height="739" alt="Dashboard" src="https://github.com/user-attachments/assets/e1a1f6a6-307e-425a-805e-d04c62a482b2" />

### 📊 Sentiment Analysis Summary :
I analyzed product-related consumer feedback using sentiment analysis libraries like **VADER SentimentIntensityAnalyzer**.  
Each review was scored for:  
- **Negative Sentiment Score**  
- **Neutral Sentiment Score**  
- **Positive Sentiment Score**  
- **Compound Score** (overall sentiment)
  
<img width="788" height="737" alt="Sentiment Score" src="https://github.com/user-attachments/assets/3f50cc63-1006-4b2d-a3b9-4b4864bc8f2e" />

  
