# import os
# import tweepy as tw
# import pandas as pd

# api_key = JdkmLfZE2TrF3sXMsH1tHbFAd
# api_key_secret = LX3jr9VilLmNKAAod9J13wEQMhcrpQoBEjhU8kPOxAYJpZVmY4
# Bearer_token = AAAAAAAAAAAAAAAAAAAAAPYTZgEAAAAArQEWeQI7kz%2B4QOTMEu6HFy5f9m8%3DOHdAt2aloezG2sNoaruDeRyFuY0bzzQFVXGVv9DSIUCvbTnPHt



# auth = tw.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tw.API(auth, wait_on_rate_limit=True)

# search_words = "#wildfires"
# date_since = "2018-11-16"

# tweets = tw.Cursor(api.search,
#               q=search_words,
#               lang="en",
#               since=date_since).items(5)

# # Iterate and print tweets
# for tweet in tweets:
#     print(tweet.text)


import tweepy
import webbrowser
import json
import pandas as pd



consumer_key = "a4gbMOkXABb1aNKH3PFEMf5XJ"
consumer_secret = "tUVwvT1FiKAPm01EKt9grkbPlZQR6saCLGHRPF8n8Ic4oxxpWL"

bearer = "AAAAAAAAAAAAAAAAAAAAAPYTZgEAAAAALjEmIMlQ5G6yQZoYUllGfpvh3%2BM%3DgHcxwmIhMMr8lZq9gP7bT3Q76ROuibsGSTqJYMOtiUHtf1p7ft"

access_token = "316522676-chP53Bq7QXhBwidS0Hnyfs7aaSqHquslXVLHJP7s"
acces_token_secret = "0ojcSS1rcfB2JkdmVdElrxrGnqvV1ztuJGwJimz9usSK2"

 
# callback_uri = 'oob'
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
# redirect_url = auth.get_authorization_url()
# #print(redirect_url)

# webbrowser.open(redirect_url)
# user_pin_input = input("What´s the pin value?")
# user_pin_input
# auth.get_access_token(user_pin_input)
# print(auth.access_token, auth.access_token_secret)



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

keyword = '2022'
limit=20

tweets = tweepy.Cursor(api.search_tweets, q=keyword, count=100, tweet_mode='extended').items(limit)

colums = ['User','Tweet']
data = []

for tweet in tweets:
    #print(tweet.full_text) 
    data.append([tweet.user.screen_name, tweet.full_text])
df = pd.set_option("display.max_colwidth", -1)
df = pd.DataFrame(data, columns=colums)
print(df)
