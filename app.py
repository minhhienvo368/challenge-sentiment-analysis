import streamlit as st
from PIL import Image, ImageOps
import pandas as pd
from utils.my_functions import *

# Page configuration
st.set_page_config(
    page_title="Sentiment analysis app",
    layout='wide',
    initial_sidebar_state="collapsed")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/css/style.css")

# make container:
header = st.container()
plots = st.container
user_testing = st.container()
footer = st.container()


st.sidebar.title('Menu Bar')
#st.sidebar.write('''39.7k tweets''')
show_list = ['Homepage','Netflix', 'SquidGame', 'TheGuilty', 'Maid', 'MidnightMass', 'YourFavouriteShow']
user_selection = st.sidebar.selectbox('Choose a Netflix show', options = show_list)

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
        input_txt = st.text_input("Enter the hashtag you want to search for on Twitter:", value="#Netflix")
        number_tweets = st.slider('How many tweets do you want to analyze? (max=1000)', 0, 1000, 100)
        hashtag_list = []
        
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
    





