import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import emoji
import re

def analyze_social_media_post(post_text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(post_text)['compound']
    
    if sentiment_score >= 0.05:
        sentiment = "Positive"
    elif sentiment_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    keywords = ["python", "social media", "analysis"]
    used_keywords = [kw for kw in keywords if kw.lower() in post_text.lower()]

    emojis = [c for c in post_text if c in emoji.UNICODE_EMOJI]

    trend_pattern = re.compile(r'\b#\w+\b')
    potential_trends = trend_pattern.findall(post_text)

    return {
        "sentiment": sentiment,
        "used_keywords": used_keywords,
        "emojis": emojis,
        "potential_trends": potential_trends
    }

post_text = "I love analyzing social media posts with Python! 😍 #DataScience #TechTuesday"
result = analyze_social_media_post(post_text)
print(result)