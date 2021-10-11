# Email Sentiment Analysis

### Steps

+ Step 1: Scraping
  Scrap the 10000 most recent English tweets with the hashtag: #queengambit.
  You can use the Twitter API (recommended) or do it with the classical scrapping methods.

+ Step 2: preprocessing
  Preprocess the data.

+ Step 3: Modeling
  Find a sentiment analysis dataset that matches your use-case. Then, create a sentiment analysis model.

+ Step 4: Evaluate your model
  Make sure your model predicts right.

+ Step 5: Predict the overall sentiment
  Now that your model is ready, extract the general sentiment out of your scrapped data.

+ Step 6: double check
  Randomly check a few tweets to verify that your model predicts the right sentiment.

+ Step 7: readme file
  Prepare a readme file with all the insights that you have gathered about the show's reactions. (brief)

+ Bonus: Make an API
  Make an API that accepts a hashtag in the route /predict.
  Run the complete pipeline to predict the sentiment out of your hashtag.
  Wrap the API in a Docker container.
  Deploy it on Heroku.
