# Imports
import os
import pandas as pd

tweet_count = 10000
text_query = "xlhome"
since_date = "2020-01-01"
until_date = "2020-12-30"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> text-query-tweets.json'.format(tweet_count, since_date, text_query, until_date))

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)

# Displays first 5 entries from dataframe
# tweets_df2.head()

# Export dataframe into a CSV
tweets_df2.to_csv('keyXlHome.csv', sep=',', index=False)


# Below are two ways of scraping using CLI commands.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# # Query by username
# # Setting variables to be used in format string command below
# tweet_count = 100
# username = "jack"

# # Using OS library to call CLI commands in Python
# os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(tweet_count, username))

# # Reads the json generated from the CLI command above and creates a pandas dataframe
# tweets_df1 = pd.read_json('user-tweets.json', lines=True)

# # Displays first 5 entries from dataframe
# # tweets_df1.head()

# # Export dataframe into a CSV
# tweets_df1.to_csv('user-tweets.csv', sep=',', index=False)


# Query by text search
# Setting variables to be used in format string command below
