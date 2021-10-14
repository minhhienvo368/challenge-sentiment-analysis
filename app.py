import streamlit as st
#import tensorflow as tf
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from PIL import Image, ImageOps
# To identify the sentiment of text
from textblob import TextBlob
import re
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

# make container:
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

def expand_tweet(twt):
    # general
    twt = re.sub(r"n\'t", " not", twt)
    twt = re.sub(r"\'re", " are", twt)
    twt = re.sub(r"\'s", " is", twt)
    twt = re.sub(r"\'d", " would", twt)
    twt = re.sub(r"\'ll", " will", twt)
    twt = re.sub(r"\'t", " not", twt)
    twt = re.sub(r"\'ve", " have", twt)
    twt = re.sub(r"\'m", " am", twt)
    # specific
    twt = re.sub(r"won\'t", "will not", twt)
    twt = re.sub(r"can\'t", "can not", twt)    
    return twt



# To fetch the sentiments using Textblob
def fetch_sentiment_using_textblob(twt):
    new_tweet = expand_tweet(twt)
    analysis = TextBlob(new_tweet)
    return 'positive' if analysis.sentiment.polarity >= 0 else 'negative'

def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.04:
        return 'positive'
    elif (lb > -0.04) and (lb < 0.04):
        return 'neutral'
    else:
        return 'negative'

with header:
    st.header("_ NLP app_")
    st.title(" Twitter Sentiment Analysis ")
    image = Image.open('assets/theguilty.jpg')
    st.image(image, width=600)
    st.write('---')

with dataset:
    st.write("With TextBlob sentiment")
    st.title(" Type your text")
    squidgame="squidgame"
    user_input = st.text_area("Give a text please: ", squidgame)
    res=fetch_sentiment_using_textblob(user_input)
    st.write('---')
    #st.write("Sentiment Analysis prediction with TextBlob")
    st.write("You've just given a", res, 'twist')

