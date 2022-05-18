import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import sys
import pickle
import tensorflow as tf
from keras.models import Sequential
from keras import layers
from keras_preprocessing.sequence import pad_sequences

gpus = tf.config.list_physical_devices(device_type = 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

if len(sys.argv)-1 != 1:
   print('no text')
   sys.exit()

corpus = [sys.argv[1]]

#CNN
with open('models/cnn/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

testset = tokenizer.texts_to_sequences(corpus)
testset=pad_sequences(testset,padding='post', maxlen=100)

maxlen=100
vocab_size=len(tokenizer.word_index)+1
embedding_dim=100
model=Sequential()

model.add(layers.Embedding(vocab_size,embedding_dim, input_length=maxlen))
model.add(layers.Conv1D(20,5,activation='relu'))
model.add(layers.GlobalMaxPooling1D())
model.add(layers.Dense(10,activation='relu'))
model.add(layers.Dense(5,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.load_weights("models/cnn/cnn");

predicition=model.predict(testset)

labels=['Action','Comedy','Drama','Romance','Thriller']
for index, isGen in enumerate(predicition[0]):
    if isGen >0.5:
        print(labels[index])