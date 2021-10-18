# To identify the sentiment of text
from textblob import TextBlob
import requests
import regex as re
import pandas as pd
from textblob import TextBlob
from emoji_translate.emoji_translate import Translator
from typing import Tuple, List
import plotly.express as px
import streamlit as st
import math
import json
import datetime
import twint
import nest_asyncio
#nest_asyncio.apply()

from wordcloud import WordCloud, STOPWORDS

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def scrape_twitter(searchterms: List, max_twt) -> pd.DataFrame:
    """
    Scrapes Twitter for tweets with a given searchterm,
    can edit the maximum amount of tweets returned.
    """
    
    tweets_for_df = []

    for search_term in searchterms:
        c = twint.Config()
        c.Search = search_term
        c.Limit = round(max*2)  # Collects more than what the user wants because we filter more after
        c.Pandas = True  # saved as a pd dataframe
        twint_df = twint.storage.panda.Tweets_df
        
        #Filter english reviews only (problem with TWINT even if selects only 'en')
        tweets_df_eng = twint_df.loc[twint_df['language'] == 'en']

    df_tweets = pd.DataFrame(data=tweets_df_eng,
                             columns=["date", "username", "tweet"])

    df_tweets = df_tweets.drop_duplicates(["tweet"])
    df_tweets = df_tweets[df_tweets["text"].str.startswith("I've just watched episode S")]
    print(f"Shape of df after dropping duplicates: {df_tweets.shape}")

    if len(df_tweets) > max_twt:
        return df_tweets.iloc[:max_twt]
    else:
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


