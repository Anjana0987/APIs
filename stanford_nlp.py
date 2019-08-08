from pycorenlp import StanfordCoreNLP
from nltk.parse import CoreNLPParser
import pandas as pd

nlp = StanfordCoreNLP('http://localhost:9000')
result = CoreNLPParser(url='http://localhost:9000')

text = "This movie was actually neither that funny, nor super witty. The movie was meh. I liked watching that movie. If I had a choice, I would not watch that movie again."
print(type(text))
data = pd.read_csv("try.csv") 
print(type(data['text']))
result = nlp.annotate(str(data['text']),
                   properties={
                       'annotators': 'sentiment, ner, pos',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
scores = []
texts = []
sentiment = []
for s in result['sentences']:
    scores.append(s['sentimentValue'])
    texts.append(" ".join([t["word"] for t in s["tokens"]]))
    sentiment.append(s['sentiment'])

    #print(" ".join([t["word"] for t in s["tokens"]]), s['sentimentValue'], s['sentiment'])  

df = pd.DataFrame()
df['text'] = texts
df['scores'] = scores
df['sentiment'] = sentiment
print(df)



