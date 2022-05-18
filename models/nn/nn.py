import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras import layers

corpus = [sys.argv[1]]

vectorizer=CountVectorizer(min_df=0,lowercase=False,max_features=10000)
x_test=vectorizer.fit_transform(corpus)
x_test_zeroes = np.zeros((1,10000,), dtype='int64')

for index, num in enumerate(x_test.data):
    x_test_zeroes[0,index] = num


inputdim=x_test_zeroes.shape[1]
model=Sequential()
model.add(layers.Dense(10,input_dim=inputdim, activation='relu'))
model.add(layers.Dense(10,input_dim=inputdim, activation='relu'))
model.add(layers.Dense(5,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.load_weights("models/nn/nn")

predicition=model.predict(x_test_zeroes)
labels=['Action','Comedy','Drama','Romance','Thriller']
for index, isGen in enumerate(predicition[0]):
    if isGen >0.5:
        print(labels[index])