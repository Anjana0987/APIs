import pandas as pd
import re
from gensim import corpora, models
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('try.csv')
text_data = data['text']

'''def count_words(sent):
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

def count_tf(d_info, freq_list):
    tf_scores = []
    for t in freq_list:
        id = t['doc_id']
        for k in t['freq_dict']:
            temp = {'doc_id' : id, 'key': k, 'TF_score' : t['freq_dict'][k]/d_info[id - 1]['doc_length']}
            tf_scores.append(temp)
    return tf_scores

def count_idf(d_info, freq_list):
    idf = []
    count = 0
    for d in freq_list:
        count += 1
        for k in d['freq_dict'].keys():
            count = sum([k in t['freq_dict'] for t in freq_list])
            temp = {'doc_id' : count, 'IDF_score' : math.log(len(d_info)/count), 'key' : k}
            idf.append(temp)
    return idf

def compute_tf_idf(tf, idf):
    tfidf_scores = []
    for j in idf:
        for i in tf:
            if j['key'] == i['key'] and j['doc_id'] == i['doc_id']:
                temp = {'doc_id' : j['doc_id'], 'TF*IDF' : j['IDF_score'] * i['TF_score'], 'key': i['key']}
                tfidf_scores.append(temp)
    return(tfidf_scores)

#for i in text_data:
    #clean_text = sent_tokenize(i)
text_sents = [preprocess(s) for s in text_data]
doc_info = get_doc(text_sents)
freq_lis = frequency(text_sents)
tf = count_tf(doc_info, freq_lis)
idf = count_idf(doc_info, freq_lis)
tf_idf = compute_tf_idf(tf, idf)
'''

vec = TfidfVectorizer(sublinear_tf=True, stop_words='english')
X = vec.fit_transform(text_data)
feature_names = vec.get_feature_names()
dense = X.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)

S = cosine_similarity(X)


