import streamlit as st
#import tensorflow as tf
import pandas as pd
from PIL import Image, ImageOps
from utils.my_functions import *

# make container:
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
footer = st.container()


with header:
    st.title(" Tweets Sentiment Analysis ")
    image = Image.open('assets/theguilty.png')
    st.image(image, width=600)
    st.write('---')

with dataset:
    st.title("Detecting your tweet with TextBlob")

    user_input = st.text_area("Type your tweet: ")
    res=fetch_sentiment_using_textblob(user_input)
    st.write("You've just given a", res, 'tweet')
    
    st.write('---')

    st.title("With Vader sentiment")
    st.write('Predict a positive or negative tweet')
    user_input1 = st.text_area("Give a text please: ")
    res1=sentiment_analyzer_scores(user_input1)
    st.write('---')
    #st.write("Sentiment Analysis prediction with TextBlob")
    st.write("You've just given a", res1, 'tweet')
