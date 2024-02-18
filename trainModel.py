import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import json
import os
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer

nltk.download('punkt')
nltk.download('wordnet')

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


with open('data/turkish_stopwords.json', encoding='utf-8') as file:
    stopwords = set(json.load(file))

lemmatizer = WordNetLemmatizer()


intents = json.loads(open('data/intents.json', encoding='utf-8').read())


checkpoint = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)


words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

training = []
output_empty = [0] * len(classes)

max_words = len(words)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)


train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])


model = Sequential()
model.add(Dense(64, input_shape=(max_words,), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(classes), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


early_stopping = EarlyStopping(monitor='loss', patience=10)


hist = model.fit(train_x, train_y, epochs=200, batch_size=20, callbacks=[early_stopping], validation_split=0.2)


model.save('models/chatbot_model.keras', hist)


final_words = [word for word in words if word not in stopwords]


with open('data/words.json', 'w', encoding='utf-8') as file:
    json.dump(final_words, file, ensure_ascii=False)


with open('data/classes.json', 'w', encoding='utf-8') as file:
    json.dump(classes, file, ensure_ascii=False)

print("words.json ve classes.json dosyaları oluşturuldu.")
print("Chatbot modeli oluşturuldu.")
