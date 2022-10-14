import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('xlhome since:2021-01-01 until:2021-12-30').get_items()):
    if i>10000:
        break
    # tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    tweets_list2.append([tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above
# tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Tweet Id', 'Text', 'Username'])
tweets_df2.to_csv('xlhomedatatahun2021.csv', sep=',', index = False)
# tweets_df2 = pd.read_json('text-tweets.json', lines=True)