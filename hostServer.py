# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, abort
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import json
import os
import pickle

app = Flask(__name__)

vectorizer = pickle.load(open('source/vector.pickel','rb'))
transformer = pickle.load(open('source/transformer.pickel','rb'))
nameDoc = json.load(open('source/nameDoc.json','rb'))['data']
tfidf = pickle.load(open('source/tfidf.pickel','rb')).toarray()
text_clf_svm = pickle.load(open('source/pipeline.pickel','rb'))

@app.route("/search", methods=['POST'])
def search():
    string = request.json['data']

    query = []

    query.append(string)

    testVectorizerArray = vectorizer.transform(query).toarray()

    transformer.fit(testVectorizerArray)

    tfidf_query = transformer.transform(testVectorizerArray)

    cosine_similarities = linear_kernel(tfidf_query, tfidf).flatten()

    related_docs_indices = cosine_similarities.argsort()[:-100:-1]

    result = []
    for doc in related_docs_indices:
        namedoc = nameDoc[doc]['name']
        category = nameDoc[doc]['class']
        direct = 'tool/source/'+category+"/"+namedoc
        f = open(direct,"rb")
        object_ = json.load(f)
        result.append(object_)
    
    return jsonify({'result':result}), 201

@app.route("/searchClass", methods=['POST'])
def searchClass():
    string = request.json['data']
    query = []
    query.append(string)
    predicted_svm = text_clf_svm.predict(query)
    return jsonify({'class': predicted_svm[0]}), 201

if __name__ == '__main__':
    app.run(debug=True)
