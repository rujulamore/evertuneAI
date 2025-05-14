from textblob import TextBlob

def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity  # -1 to 1
