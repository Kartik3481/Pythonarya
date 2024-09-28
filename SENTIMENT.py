from vadersentiment.vadersentiment import SentimentIntensityAnalyzer
Analyzer = sentimentIntensityAnalyzer()

def analyze(text):
    try:
        sentiment= Analyzer.polarity_scores(text)
        
       if sentiment("compound") >= 0.05:
           print("positive")
       elif sentiment9"compound") <= -0.05:
           print("Negative")
       else:
           print("Neutral")
    except Exception as e:
        print(e)

Text= input("PLEASE ENTER A TEXT:")
analyze(Text)