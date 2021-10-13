# NLP Sentiment Analysis

______________________________________________________________________________________________________________________________________________________
![logo](assets/netflix_logo.jpeg | width="400" height="200")
______________________________________________________________________________________________________________________________________________________


- Developer Name: `Minh Hien Vo`
- Level: `Junior Data Scientist`
- Duration: `4 days`
- Deadline : `14/10/21 16:00`
- Team challenge: `Solo project`
- Type of challenge: `Learning and Practising`
- Promotion : `Arai2.1`
- Coding Bootcamp: `Becode Artificial Intelligence (AI) Bootcamp`
![logo](assets/giphy.gif |height="100")

## Mission Objectives
- Be able to scrapped at least 10000 tweets in English containing the hashtag of a series or movie.
- Be able to apply data preprocessing (e.g. tokenization, stemming and lemmatization) for exploration of text-based datasets.
- Be able to evaluate the performance of pre-trained models.
- Be able to predicted an overall sentiment out of all those tweets.
- Be able to do the development and deployment of the dashboard for text summarization.

____________________________________________________________________________________________________________________________________________

## About The Repository

This is a project about developing a Natural language processing model that is able to predict an overall sentiment out of all tweets with a specific hashtag on Twitter. 


____________________________________________________________________________________________________________________________________________


## R E P O S I T O R Y

**README.md**
  - describe all of infos about the project

**app.py**
  - using streamlit library


**Procfile**
  - Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
  - This Procfile is used to declare a variety of process types, including: the app's web server.

**requirements.txt**
  - is a txt file used for specifying what python packages are required to run this project

**assets folder**
 
**data folder**
  - this is where the logo is saved
  - this is also where the **summary.txt** is saved, which gives the user the option to download the summary as a txt file
      
______________________________________________________________________________________________________________________________________________________

## Libraries Used For This Project


**Pandas** https://pypi.org/project/pandas/
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

**Time** https://docs.python.org/3/library/time.html
  - Time module handles time-related tasks.
  - In this project, time is used to calculate the total time the code runs.


**Typing** https://docs.python.org/3/library/typing.html
  - Typing defines a standard notation for Python function and variable type annotations.
  - In this project, typing is used to help document the code properly.

**Heroku** //www.heroku.com
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
  - In this project, Heroku is used to deploy the app but due to limited GB since we are only using the free version, it was returning an error that the slug size is too big.
  - As free users of Heroku, we are only allowed of up to 500MB slug size.
  - Everything is already in the repository, the Procfile and the requirements.txt, we just need a bigger slug size to deploy it
![image](g)


______________________________________________________________________________________________________________________________________________________

## Clone / Fork This Repository
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.


![Thank you]()
### Thank you for reading. Have fun with the code! 🤗


+ Nice to have: 
  Make an API that accepts a hashtag in the route /predict.
  Run the complete pipeline to predict the sentiment out of your hashtag.
  Wrap the API in a Docker container.
  Deploy it on Heroku.

