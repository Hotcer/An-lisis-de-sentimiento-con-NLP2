from textblob import TextBlob

# Función de analisis de sentimiento:

def sentiment_analysis(text):
   analysis = TextBlob(text)
   if analysis.sentiment.polarity < 0:
      return 0 #negative
   elif analysis.sentiment.polarity == 0:
      return 1 #neutral
   else:
      return 2 #positive