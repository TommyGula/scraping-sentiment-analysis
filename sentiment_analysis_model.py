#Import libraries
import nltk
from nltk.corpus import movie_reviews
import random
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing import sequence
import tensorflow as tf
import matplotlib.pyplot as plt
import sklearn as skl
import math
from sklearn.metrics import confusion_matrix

#Creates a bag of words
def bag_of_words(df, clear_words):
    bag = {}
    count = 1
    for y in df:        
        for i in y:
            if i in bag.keys():
                continue
            elif i in clear_words:
                continue
            else:
                bag[i] = count
                count += 1
    return bag

#A function that encodes our data. Every word from every sentence 
#is replaced with it's key from our bag of words
def encode(bag, docs):
    general_list = []
    for y in docs:
        bad = 0
        sentence = []
        for i in range(max_length):
            if i >= len(y):
                sentence.insert(0,0)
            else:
                if y[i] in clear_words:
                    bad += 1
                    continue
                if y[i] in bag.keys():
                    sentence.append(bag[y[i]])
                else:
                    sentence.append(0)
        for g in range(bad):
            sentence.insert(0,0)
        general_list.append(sentence)
    return general_list


#Create DataFrame
documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
docs = pd.DataFrame(documents)


#Transform DataFrame
docs.columns = ['Words', 'Sentiment']
docs['Sentiment'] = np.where(docs['Sentiment'] == 'pos', 1, 0)


#Create bag of words
max_length = 750
clear_words = ['''"''', ',', ';', '.', ':', '-', '/', '*', ')', '(']
bag = bag_of_words(docs['Words'], clear_words)


#Building the model according to out params
def build_model(bag, max_length, X_train, X_test, y_train, y_test):
    model = tf.keras.models.Sequential()
    model.add(
        tf.keras.layers.Embedding(
            input_dim = len(bag) + 1, # The size of our vocabulary 
            output_dim = 32, # Dimensions to which each words shall be mapped
            input_length = max_length # Length of input sequences
        )
    )
    model.add(
        tf.keras.layers.Dropout(
            rate=0.25 # Randomly disable 25% of neurons
        )
    )
    model.add(
        tf.keras.layers.LSTM(
            units=32 # 32 LSTM units in this layer
        )
    )
    model.add(
        tf.keras.layers.Dropout(
            rate=0.25 # Randomly disable 25% of neurons
        )
    )
    model.add(
        tf.keras.layers.Dense(
            units=1, # Single unit
            activation='sigmoid' # Sigmoid activation function (output from 0 to 1)
        )
    )
    model.compile(
        loss=tf.keras.losses.binary_crossentropy, # loss function
        optimizer=tf.keras.optimizers.Adam(), # optimiser function
        metrics=['accuracy']) # reporting metric
    history = model.fit(
        X_train, y_train,            
        batch_size=100, 
        epochs=6,
        validation_split=0.2,
        verbose=1
    )
    return model


#Preparing-input functions
def convert(sentence):
    list = []
    list.append(sentence.split())
    return list
def correct(sentence, clear):
    return ''.join(x for x in sentence if x not in clear).lower()
def concat_sentence(sentence, length):
    s_len = len(sentence)
    if s_len > length:
        return sentence

    else:
        return (sentence + " ") * math.ceil(length / s_len) 

'''        for i in range(math.ceil(length / s_len)):
            sentence = sentence + " " + sentence
        return sentence

'''
#Prediction functions
def predict_one(sentence, model):
    sentence = concat_sentence(sentence, max_length)
    corrected_sentence = np.array(convert(correct(sentence, clear_words)))
    encoded_sentence = encode(bag, corrected_sentence)
    prediction = model.predict(encoded_sentence)
    return prediction
def scrape_and_predict(reviews, model):
    reviews = reviews
    predictions_dict = {}
    for i in reviews['review']:
        sentence = concat_sentence(i, max_length)
        corrected_sentence = np.array(convert(correct(sentence, clear_words)))
        encoded_sentence = encode(bag, corrected_sentence)
        prediction = model.predict(encoded_sentence)
        predictions_dict[i] = prediction[0][0]
    reviews['predicted'] = predictions_dict.values()
    reviews['predicted_binary'] = np.where(reviews['predicted'] >= 0.5, 1, 0)
    reviews['rating_binary'] = np.where(reviews['rating'].astype(int) >= 5, 1, 0)

    conf = confusion_matrix(reviews['rating_binary'], reviews['predicted_binary'])
    return reviews, conf


#Preparing model if required
def get_model():
    #Preparing data
    encoded_column = np.array(encode(bag, docs['Words']))
    X_train, X_test, y_train, y_test = skl.model_selection.train_test_split(encoded_column, docs['Sentiment'].values, test_size=0.2, random_state=1)

    #Getting our model
    model = build_model(bag, max_length, X_train, X_test, y_train, y_test)

    #Returning model
    return model

