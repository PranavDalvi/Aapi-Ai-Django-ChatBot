
import re
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, HttpResponse
import random
import json
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
#from .models import Response, models

# Remove the comments to download additional nltk packages
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# from sklearn.feature_extraction.text import TfidfVectorizer

from tensorflow import keras
import tensorflow
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

def index(request):
   return render(request , 'chatbot_project/index.htm')


def chatBot(request):
   query = str(request.GET.get("query"))
   # print(query)
   lemmatizer=WordNetLemmatizer()

   with open('jsonfile.json') as fileobj:
      readobj=json.load(fileobj)

   words=[]
   classes=[]
   documents=[]
   stop_words=['is','and','the','a','are','i','it']
   cleaned_word=[]

   for intent in readobj['intents']:
      for pattern in intent['patterns']:
         word_list=word_tokenize(pattern)
         words.extend(word_list)
         documents.append((word_list,intent['tag']))
         if intent['tag'] not in classes:
               classes.append(intent['tag'])

   # vectorizer = TfidfVectorizer()
   # X = vectorizer.fit_transform(cleaned_word)

   words = sorted(set(words))
   classes = sorted(set(classes))

   def clean_corpus(words):
      words = [doc.lower() for doc in words]
      for w in words:
         if w not in stop_words and w.isalpha():
               w=lemmatizer.lemmatize(w)
               cleaned_word.append(w)
      return(cleaned_word)

   cleaned_list = clean_corpus(words)

   words = sorted(set(words))
   classes = sorted(set(classes))
   # y = encoder.fit_transfrom(np.array(classes), reshape(-1, 1))

   training =[]
   output_empty = [0] * len(classes)


   for document in documents:
      bag =[]
      word_patterns = document[0]

      word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

      for word in words :
         bag.append(1) if word in word_patterns else bag.append(0)
      output_row = list(output_empty)
      output_row[classes.index(document[1])] = 1 
      training.append([bag,output_row])

   '''Neural Network'''
   random.shuffle(training)
   training = np.array(training,dtype=object)
   train_x = list(training[:,0])
   train_y = list(training[:,1])

   model = Sequential([Dense(128, input_shape = (len(train_x[0]),),activation='relu'),Dropout(0.2),Dense(64, activation='relu'),Dropout(0.2),Dense(len(train_y[0]),activation = 'softmax')])
   sgd = tensorflow.keras.optimizers.SGD(learning_rate=0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
   model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
   history = model.fit(np.array(train_x),np.array(train_y),epochs=20,batch_size=1,verbose=7)
   # model.save('chatbot_model.model',history)


   def cleaning_up_message(message):
      message_word = word_tokenize(message)
      message_word = [lemmatizer.lemmatize(word.casefold()) for word in message_word]
      return message_word


   def bag_of_words(message):
      message_word = cleaning_up_message(message)
      bag = [0]*len(words)
      for w in message_word:
         for i, word in enumerate(words):
               if word == w:
                  bag[i] = 1
      return np.array(bag)
      
   INTENT_NOT_FOUND_THRESHOLD = 0.25

   def predict_intent_tag(message):
      BOW = bag_of_words(message)
      res = model.predict(np.array([BOW]))[0]
      results = [[i,r] for i,r in enumerate(res) if r > INTENT_NOT_FOUND_THRESHOLD ]
      results.sort(key = lambda x : x[1] , reverse = True)
      return_list = []
      for r in results:
         return_list.append({ 'intent': classes[r[0]], 'probability': str(r[1]) })
      return return_list

   def get_response(intents_list , intents_json):
      tag = intents_list[0]['intent']
      list_of_intents = intents_json['intents']
      for i in list_of_intents:
         if i['tag'] == tag :
               result= random.choice (i['responses'])
               break
         # elif i['tag']!=tag:
         #     result=random.choice(["Invalid response","Sorry:), I didn't get what you are saying","Pardon me..!"])
         #     break
      return result

   print(" Aapi is Running ! ")
   message = query
   ints = predict_intent_tag(message)
   bot_response = get_response(ints, readobj)
   # print(bot_response)
   return JsonResponse({"Bot": bot_response})
   
