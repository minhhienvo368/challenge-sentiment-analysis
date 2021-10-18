import streamlit as st
from PIL import Image, ImageOps
import pandas as pd
from utils.my_functions import *
import matplotlib.pyplot as plt
import twint

# Page configuration
st.set_page_config(
    page_title="Sentiment analysis app",
    layout='wide',
    initial_sidebar_state="collapsed")
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("assets/css/style.css")

# make container:
header = st.container()
plots = st.container
user_testing = st.container()
footer = st.container()


st.sidebar.title('Menu Bar')
#st.sidebar.write('''39.7k tweets''')
show_list = ['Homepage','Netflix', 'SquidGame', 'TheGuilty', 'Maid', 'MidnightMass', 'YourFavouriteShow']
user_selection = st.sidebar.selectbox('Choose a Netflix show', options = show_list)
st.sidebar.write("Interested in this project?"
                 "\nVisit my [Github](https://github.com/minhhienvo368/challenge-sentiment-analysis)")

if user_selection == "Homepage": 
    with header:
        st.title("Predict a tweet sentiment by user")
        st.write("This form can detect a positive/negative tweet, using TextBlob")
    
        form1 = st.form(key='formTextBlob')
        twt1 = form1.text_input('Enter your tweet')
        submit = form1.form_submit_button('Go')

        res1=fetch_sentiment_using_textblob(twt1)
        output1 = '<p style="font-family:Courier; color:Blue; font-size: 16px;">Result: </p>'
        st.markdown(output1, unsafe_allow_html=True)    
        st.write("You've just given a", res1, 'tweet')
        st.write('---')

        st.write("This form can detect a positive/neutral/negative tweet, using Vadersentiment")
        form2 = st.form(key='formVadersentiment')
        twt2 = form2.text_input('Enter your tweet')
        submit = form2.form_submit_button('Go')
        res2=sentiment_analyzer_scores(twt2)

        st.markdown(output1, unsafe_allow_html=True)
        st.write("You've just given a", res2, 'tweet')

elif user_selection == "YourFavouriteShow":
    with header:
        st.title("Analyze your own favorite show")
        image = Image.open('assets/guess_your_show.jpeg')
        st.image(image)
        st.write('You can put your favourite show here, we will give you the interesting analytical information relating to the show')
        st.write('---')
    
    # Handles the second option from the sidebar.
    # Scrapes a searchterm given by the user.
    # Shows a piechart with useful info on sentiment analysis.
        input_txt = st.text_input("Enter the hashtag of a series on Twitter:", value="#")
        number_tweets = st.slider('How many tweets do you want to analyze? (max=1500)', 0, 1500, 100)
        
        st.write(f'Current hashtags: __{input_txt}__')  
        col1, col2, col3 = st.columns(3)
        # Button to scrape and analyze
        if col2.button('Fetch it!') and number_tweets >= 1:
            with st.spinner('In progress ...'):
                # if number_tweets > 1:
                #     st.write(f"*Summary:* {str(number_tweets)} tweets about __{input_txt}__ are being scraped and analyzed.")
                # elif number_tweets == 1:
                #     st.write(f"*Summary:* 1 tweet about __{input_txt}__ is being scraped and analyzed.")
                st.write(f"*Summary:* {str(number_tweets)} tweets about __{input_txt}__ are being scraped and analyzed.")
                st.write("*Scraping the tweets ...*")
                df = scrape_twitter(input_txt, number_tweets)  
                st.write("*Preprocessing the tweets ...")
                df['tweet_cleaned'] = df['tweet'].apply(lambda x: expand_tweet(x))
                df['tweet_cleaned'] = df['tweet_cleaned'].apply(lambda x: preprocess_tweet(x))

                st.write("Labeling tweets ...")
                df['sentiment'] = df['tweet_cleaned'].apply(lambda x: calcul_sentiment_score(x))
                df = df.reset_index(drop=True)
                st.success('Success!')
                # Presenting the dataframe and sentiment analysis plot
            
                st.markdown(f"<h3 style='text-align: center;'>Sentiment Analysis of {input_txt}</h3>", unsafe_allow_html=True)
                st.write(df)
                csv = convert_df(df)
                st.write('')

                # Plots sentiment analysis
                fig = px.histogram(df, x=df.sentiment)
                fig.update_layout(title_text="Sentiment Score Distribution", title_x=0.5)
                fig.update_xaxes(title_text='Sentiment score from 1 (negative) to 5 (positive)')
                fig.update_yaxes(title_text='Count')
                fig.update_layout(bargap=.1)
                st.plotly_chart(fig)

                score = df.sentiment.mean()
                # Showing average sentiment score
                st.metric(label="Average Sentiment Score", value=f"{round(score,2)}/5")
                df_positive = df[df['sentiment'] > 3]
                df_negative = df[df['sentiment'] < 3]
                df_neutral = df[df['sentiment'] == 3]

            # Checks if enough positive and negative tweets for the wordcloud (minimum 1 tweet in each)
            if len(df_positive.index) > 0 and len(df_negative.index) > 0:
                # Showing wordcloud (All, Positive and Negative)
                st.markdown(f"<h4 style='text-align: center;'>WordClouds of {input_txt}</h4>",
                            unsafe_allow_html=True)

                tweet_All = " ".join(tweet for tweet in df['tweet_cleaned'])
                tweet_pos = " ".join(tweet for tweet in df_positive['tweet_cleaned'])
                tweet_neg = " ".join(tweet for tweet in df_negative['tweet_cleaned'])
                tweet_neu = " ".join(tweet for tweet in df_neutral['tweet_cleaned'])

                fig, ax = plt.subplots(3, 1, figsize=(30, 30))
                # Create and generate a word cloud image
                wordcloud_POS = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_pos)
                wordcloud_NEG = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_neg)
                wordcloud_NEU = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_neu)

                ax[1].imshow(wordcloud_POS, interpolation='bilinear')
                ax[1].set_title('Positive Tweets', fontsize=30, pad=20)
                ax[1].axis('off')
                
                ax[1].imshow(wordcloud_NEU, interpolation='bilinear')
                ax[1].set_title('Positive Tweets', fontsize=30, pad=20)
                ax[1].axis('off')

                ax[2].imshow(wordcloud_NEG, interpolation='bilinear')
                ax[2].set_title('Negative Tweets', fontsize=30, pad=20)
                ax[2].axis('off')

                st.pyplot(fig)

            else:
                # Showing all of them at once (because not enough in either positive or negative)
                st.markdown(f"<h4 style='text-align: center;'>WordCloud of {input_txt}</h4>",
                            unsafe_allow_html=True)

                tweet_All = " ".join(tweet for tweet in df['tweet_cleaned'])
                wordcloud_ALL = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(tweet_All)

                # Create and generate a word cloud image
                fig, ax = plt.subplots(figsize=(30, 30))
                ax.imshow(wordcloud_ALL, interpolation='bilinear')
                ax.set_title('All Tweets', fontsize=30, pad=20)
                ax.axis('off')

                st.pyplot(fig)

            st.write('')
            col1, col2, col3 = st.columns(3)
            # Downloads dataframe as csv if button push
            col2.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Twitter_scraped_data.csv',
                mime='text/csv')

elif user_selection in show_list[1:6]:
    with header:
        show_banner = Image.open(f'./assets/{user_selection.lower()}_banner.jpg')
        st.image(show_banner, use_column_width=True)
        st.write('---')
        df = pd.read_csv(f"./data/df_{user_selection.lower()}_labeled.csv")
        with st.spinner(f"""
        Processing {len(df)} tweets
        """):
            st.success(f"Processed {len(df)} tweets, using Vadersentiment model")
        fig = px.pie(df, values=df.sentiment3cat.value_counts(), names=df.sentiment3cat.value_counts().index, title=f'{user_selection} Sentiment Analysis', color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig, use_container_width=True)
    





