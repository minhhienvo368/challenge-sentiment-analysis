# To identify the sentiment of text
from textblob import TextBlob
import requests
import regex as re
import pandas as pd
from textblob import TextBlob
from emoji_translate.emoji_translate import Translator
from typing import Tuple, List
import plotly.express as px
import math
import json
import datetime
import twint
import string
import emoji
import nest_asyncio
import torch
#import spacy
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

#nest_asyncio.apply()

from wordcloud import WordCloud, STOPWORDS

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


def hashtag_preprocess(text):
    clean_hashtag = ''
    for char in text:
        if char not in string.punctuation and not emoji.is_emoji(char) and char.isalpha():
            clean_hashtag += char
    cleaned_hashtag = clean_hashtag.replace(' ', '')
    return cleaned_hashtag

def scrape_twitter(searchterms: str, nr_twt) -> pd.DataFrame:
    """
    Scrapes Twitter for tweets with a given searchterm,
    can edit the maximum amount of tweets returned.
    """
    c = twint.Config()
    c.Lang = 'en'
    c.Search = searchterms
    c.Limit = round(nr_twt*1.6)  # Collects more than what the user wants because we filter more after
    c.Pandas = True  # saved as a pd dataframe
    twint.run.Search(c)

    df = twint.storage.panda.Tweets_df
    
    #Filter english reviews only (problem with TWINT even if selects only 'en')
    df = df[df['language'] == 'en']
    df_tweets = pd.DataFrame(data=df, columns=["date", "username", "tweet"])
    return df_tweets

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

# Using BERT pretrained model to analyzes tweet and gives sentiment score (1-5) 
# Loads tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def calcul_sentiment_score(tweet):
    tokens = tokenizer.encode(tweet, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1


# To fetch the sentiments using Textblob - 2 categories
def fetch_sentiment_using_textblob(twt):
    new_tweet = expand_tweet(twt)
    analysis = TextBlob(new_tweet)
    return 'positive' if analysis.sentiment.polarity >= 0 else 'negative'

# To fetch the sentiments using Vadersentiment - 3 categories
def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.04:
        return 'positive'
    elif (lb > -0.04) and (lb < 0.04):
        return 'neutral'
    else:
        return 'negative'

def preprocess_tweet(tweet: str) -> str:
    """
    Handles the entire preprocessing step for one tweet,
    to pass it to a 'sentiment-analysis'-model.
    """
    hashtag = re.compile(r"^#\S+|\s#\S+")
    at_someone = re.compile(r"^@\S+|\s@\S+")
    url = re.compile(r"https?://\S+")
    tweet_without_hashtag = hashtag.sub(' ', tweet)
    tweet_without_at_and_hashtag = at_someone.sub(' person', tweet_without_hashtag)
    cleaned_text = url.sub(" fan", tweet_without_at_and_hashtag)

    cleaned_text_lower = cleaned_text.strip().lower()
    cleaned_text_lower_splitted = cleaned_text_lower.split()
    if cleaned_text_lower_splitted == "rt":
        cleaned_text_lower = " ".join(cleaned_text_lower_splitted[1:])

    emo = Translator(exact_match_only=False)
    cleaned_text_lower_emojiless = emo.demojify(cleaned_text_lower)

    clean_text = TextBlob(cleaned_text_lower_emojiless).correct()
    return str(clean_text)

def get_tweet_sentiment(tweet: str) -> float:
    """ Given a sentence, returns the polarity between -1 and 1 """
    analysis = TextBlob(tweet)
    return analysis.polarity

# Converts df to csv
def convert_df(df):
    return df.to_csv().encode('utf-8')
