"""
Simple Chatbot using NLTK

This script implements a basic chatbot using Natural Language Toolkit (NLTK).
It uses tokenization and a simple algorithm to match user input to potential
responses.
"""

import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "hey")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response, sentences):
    robo_response = ''
    sentences.append(user_response)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences)
    cosine_vals = cosine_similarity(vectors[-1], vectors)
    idx = cosine_vals.argsort()[0][-2]
    flat = cosine_vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response += "I am sorry! I don't understand you"
    else:
        robo_response += sentences[idx]
    sentences.remove(user_response)
    return robo_response

def chatbot_response(text, sentences):
    user_response = text.lower()
    if user_response != 'bye':
        if user_response in ['thanks', 'thank you']:
            return "You're welcome!"
        elif greeting(user_response):
            return greeting(user_response)
        else:
            return response(user_response, sentences)
    else:
        return "Bye! Take care."

sentences = ["your corpus of sentences", "more sentences for matching", "keep adding as many as you need"]
user_input = input("User: ")
print("Bot:", chatbot_response(user_input, sentences))
