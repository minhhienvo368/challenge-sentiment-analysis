# NLP Sentiment Analysis

______________________________________________________________________________________________________________________________________________________
![test image size](assets/netflix_logo.jpeg)
______________________________________________________________________________________________________________________________________________________

- Developer Name: `Minh Hien Vo`
- Level: `Junior Data Scientist`
- Duration: `4 days`
- Deadline : `14/10/21 16:00`
- Team challenge: `Solo project`
- Type of challenge: `Learning and Practising`
- Promotion : `Arai2.31`
- Coding Bootcamp: `Becode Artificial Intelligence (AI) Bootcamp`
____________________________________________________________________________________________________________________________________________

## Mission Objectives
- Be able to scrapped at least 10000 tweets in English containing the hashtag of a series or movie.
- Be able to apply data preprocessing (e.g. tokenization, stemming and lemmatization) for exploration of text-based datasets.
- Be able to evaluate the performance of pre-trained models.
- Be able to predicted an overall sentiment out of all those tweets.
- Be able to do the development and deployment of the dashboard for text summarization.
____________________________________________________________________________________________________________________________________________

## Data sources:
  + Source: Twitter
  + Tweets: 39.7k
  + Language: English
   
| Netflix Show | Nº Tweets scraped |
|--------------|-----------|
| Squid Game   | 23956      |
| Netflix Platform | 3456    |
| The Guilty    | 1444     |
| Midnight Mass | 7690     |
| Maid     | 3133       |
## About The Repository

This is a project about developing a Natural language processing model that is able to predict an overall sentiment out of all tweets with a specific hashtag on Twitter. The Twint library has been used to fetch the tweets five hashtags corresponding to five series or movies from Twitter (39.7k tweets in total). Then by empoyed some preprocessing techniques,  the tweets have been cleaned. Then the pretrained sentiment models (e.g. TextBlob, Vader) have been used to predict or to label the dataframe.

<img src="assets/giphy.gif" width=10% height=10%>

_________________________________________________________________________________________________________________________________________

**README.md**
  - describe all of infos about the project

**app2model.py**
  - using streamlit library

**Procfile**
  - Streamlit apps include a Procfile that specifies the commands that are executed by the app on startup.
  - This Procfile is used to declare a variety of process types, including: the app's web server.

**requirements.txt**
  - is a txt file used for specifying what python packages are required to run this project

**assets folder**
  - Contain all of images, logos using in the project

**data folder**
  - Contains the csv files
      
______________________________________________________________________________________________________________________________________________________
### Libraries
  - Pandas
  - Twint
  - Textblob 
  - Vadersentiment
  - Plotly
  - PIL


### Sentiment Analysis Models: TextBlob, Vader 
______________________________________________________________________________________________________________________________________________________

### Clone / Fork This Repository
  If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.

+ [Link of app](https://share.streamlit.io/minhhienvo368/sentiment_analysis_tweets/app.py) 
