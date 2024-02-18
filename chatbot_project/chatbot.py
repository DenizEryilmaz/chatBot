import numpy as np
import random
import json
from tensorflow.keras.models import load_model
from nltk.stem import WordNetLemmatizer
import nltk
from functions import *


def clean_up_sentence(sentence, lemmatizer):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence, lemmatizer)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,word in enumerate(words):
            if word == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % word)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list

def get_response(intents, tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            if 'function' in intent:
                return globals()[intent['function']]()
            else:
                return random.choice(intent['responses'])
    return "Üzgünüm, anlayamadım. Başka bir soru sorabilir misiniz?"


model = load_model('models/chatbot_model.keras')
intents = json.loads(open('data/intents.json', encoding='utf-8').read())
words = json.loads(open('data/words.json').read())
classes = json.loads(open('data/classes.json').read())


user_data = json.loads(open('data/user_data.json').read())


lemmatizer = WordNetLemmatizer()


print("Hoş geldiniz, lütfen yapmak istediğiniz işlemi kısaca giriniz.")
while True:
    sentence = input("- ")
    if sentence.lower() == 'exit':
        break
    ints = predict_class(sentence, model)
    tag = ints[0][0] if ints else None
    print(get_response(intents, tag))
