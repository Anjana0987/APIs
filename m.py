import pandas as pd
import re
from gensim import corpora, models
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import math

data = pd.read_csv('try.csv')
text_data = data['text']

def count_words(sent):
    count = 0
    words = word_tokenize(sent)
    for word in words:
        count = count + 1
    return count

def preprocess(data):
    stripped = re.sub('[^\w\s]', '', data)
    stripped = re.sub('_', '', stripped)
    stripped = re.sub('\s+', ' ', stripped)
    stripped = stripped.strip()
    return stripped

def frequency(data):
    i = 0
    freq_list = []
    for word in data:
        i += 1
        freq_dic = {}
        words = word_tokenize(word)
        for w in words:
            w = w.lower()
            if w in freq_dic:
                freq_dic[w] += 1
            else:
                freq_dic[w] = 1
            temp = {'doc_id' : i, 'freq_dict' : freq_dic}
        freq_list.append(temp)
    return freq_list

def get_doc(data):
    doc_info = []
    i = 0
    for w in text_sents:
        i  = i+1
        count = count_words(w)
        temp = {'doc_id' : i, 'doc_length': count}
        doc_info.append(temp)
    return doc_info



#for i in text_data:
    #clean_text = sent_tokenize(i)
text_sents = [preprocess(s) for s in text_data]
doc_info = get_doc(text_sents)
freq_lis = frequency(text_sents)
print(freq_lis)
      
   



'''DF = {}

text_data = preprocess(list(text_data))

for i in range(len(text_data)):
    sentences = text_data[i]
    #words.append(re.split(r' *[\.\?!][\'"\)\]]* *', sentences))
    for word in sentences.split():
        try:
            DF[word].add(i)
        except:
            DF[word] = {i}
            tf_idf = {}'''



