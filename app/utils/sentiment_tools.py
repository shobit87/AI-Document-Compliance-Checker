from textblob import TextBlob

def get_sentiment_score(text: str) -> str:
    """
    Calculates polarity-based sentiment (positive, neutral, or negative).
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"
