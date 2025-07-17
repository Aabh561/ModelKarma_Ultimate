from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text: str) -> str:
        
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.2:
            return "positive"
        elif polarity < -0.2:
            return "negative"
        return "neutral"
