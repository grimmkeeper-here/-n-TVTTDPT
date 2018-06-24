# -*- coding: utf-8 -*-
import json
import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

doc_name = []
doc_description =[]

stopwords_direc ='tool/stopword/stopwords.txt'
f = open(stopwords_direc)
data = json.load(f)
stopwords = data["data"]

vectorizer = CountVectorizer(ngram_range=(1, 4),stop_words=stopwords,max_features=3000, min_df = 1)
transformer = TfidfTransformer()
text_clf_svm = Pipeline([('vect', vectorizer),('tfidf', transformer),('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])

direct = 'tool/source/'
files = os.listdir(direct)
for file_ in files:
    file_direct = direct + file_
    docs = os.listdir(file_direct)
    for doc in docs:
        doc_ = {'name':doc,'class':file_}
        doc_name.append(doc_)
    doc = [file_direct +'/'+ doc for doc in docs]
    for doc_ in doc:
        f = open(doc_)
        data = json.load(f)
        tempObject = {"feature":data["description"],"target":file_}
        doc_description.append(tempObject)
df_train = pd.DataFrame(doc_description)


trainVectorizerArray=vectorizer.fit_transform(df_train.feature)
transformer.fit(trainVectorizerArray)
tfidf = transformer.transform(trainVectorizerArray.toarray())
text_clf_svm.fit(df_train.feature, df_train.target)

pickle.dump(vectorizer, open("source/vector.pickel", "wb"))
pickle.dump(transformer, open("source/transformer.pickel", "wb"))
pickle.dump(tfidf, open("source/tfidf.pickel", "wb"))
pickle.dump(text_clf_svm, open("source/pipeline.pickel", "wb"))
json.dump({'data':doc_name},open("source/nameDoc.json", "wb"))

print "done"




