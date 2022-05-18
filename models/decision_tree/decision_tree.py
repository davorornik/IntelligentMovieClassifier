import sys
import pandas as pd
import numpy as np
import tensorflow as tf
import scipy
import pickle
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras import layers
from keras.preprocessing.text import Tokenizer
labels=['Action','Comedy','Drama','Romance','Thriller']

if len(sys.argv)-1 != 1:
    print('no text')
    sys.exit()

corpus = [sys.argv[1]]

loaded_model = pickle.load(open("models/decision_tree/decision_tree.sav", 'rb'))

vectorizer=CountVectorizer(min_df=0,lowercase=False,max_features=10000)
x_train=vectorizer.fit_transform(corpus)
x_train_zeroes = np.zeros((1,10000,), dtype='int64')

for index, num in enumerate(x_train.data):
    x_train_zeroes[0,index] = num

predicition=loaded_model.predict(x_train_zeroes)
for index, isGen in enumerate(predicition[0]):
    if isGen ==1:
        print(labels[index])
        sys.exit()