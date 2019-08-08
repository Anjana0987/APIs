import csv
import pandas as pd
import spacy

nlp = spacy.load('en')

with open('try.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        text = row[2]
        doc = nlp(text)
        for token in doc:
            print('"' + token.text + '"')
