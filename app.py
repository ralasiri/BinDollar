# app.py
from flask import Flask, render_template
import tweepy
import config

app = Flask(__name__)

# Twitter API v1.1 authentication
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to fetch tweets
def get_tweets(stock_tag):
    try:
        tweets = api.user_timeline(screen_name='@BinDollarSign', count=10, tweet_mode='extended')
        stock_tweets = [tweet.full_text for tweet in tweets if stock_tag in tweet.full_text]
        return stock_tweets
    except Exception as e:  # Catching general exceptions
        print(f"Error: {e}")
        return []

@app.route('/')
def index():
    tsla_tweets = get_tweets('$TSLA')
    amzn_tweets = get_tweets('$AMZN')
    pltr_tweets = get_tweets('$PLTR')
    baba_tweets = get_tweets('$BABA')
    return render_template('index.html', tsla_tweets=tsla_tweets, amzn_tweets=amzn_tweets, pltr_tweets=pltr_tweets, baba_tweets=baba_tweets)

if __name__ == '__main__':
    app.run(debug=True)
