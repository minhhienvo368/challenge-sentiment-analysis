import streamlit as st
#import tensorflow as tf
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from PIL import Image, ImageOps
# To identify the sentiment of text
from textblob import TextBlob
import re
# make container:
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def listToString_1(s):
    # initialize an empty string
    # print("s = ", s)
    str1 = ""
    count = 0
    # traverse in the string
    for ele in s:
        if count == 0:
            str1 = str1 + str(ele)
            count = count + 1
        else:
            str1 = str1 + "" + str(ele)
            count = count + 1

    # return string
    # print('str1 = ',str1)
    return str1



# To fetch the sentiments using Textblob
def fetch_sentiment_using_textblob(tweet):
    new_tweet = decontracted(tweet)
    analysis = TextBlob(new_tweet)
    return 'positif' if analysis.sentiment.polarity >= 0 else 'negatif'


with header:
    st.header("_ Header  _")
    st.title(" Sentiment - Analysis ")
    image = Image.open('assets/giphy.gif')
    st.image(image, width=600)
    st.write('---')

with dataset:
    st.header(" Dataset ")
    st.title(" Text for prediction ")
    quidgame="quidgame"
    user_input = st.text_area("Give a text please: ", quidgame)
    res=fetch_sentiment_using_textblob(user_input)
    st.write('---')
    st.write("Sentiment's prediction")
    st.write("Prediction   :   ", res)