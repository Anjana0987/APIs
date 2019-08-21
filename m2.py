'''from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = pd.read_csv('try.csv')
text_data = data['text']

vec = TfidfVectorizer(sublinear_tf=True, stop_words='english')
X = vec.fit_transform(text_data)
feature_names = vec.get_feature_names()
dense = X.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)

S = cosine_similarity(X)

print(df)'''

import fiona
with fiona.open('shpfiles/MyShapefile.shp') as shp:
     # schema of the shapefile
     print(shp.schema)