import tweepy
from textblob import TextBlob
import os
import csv

#The first step is authorization with twitter
consumer_key = 'kiqB6Vx0h9UcUOkddsYa9Cg9w'
consumer_secret = '8QFyq3BbL2kB02ObzUISe7xMoWDZZ8hWBVklomSoi70oDsyQEN'

access_token = '1015381438378569729-aQ6OpIl82lWU1F4JkcP3noZZsOLULA'
access_token_secret = '4a88IjKoKZpYQs1AUyp5fBSn9xeZuNqOAmj0k5LIvKvCl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Then make the twitter API variable
api = tweepy.API(auth)

#Now can do things like create and delete tweets, or find and twitter users

#Searching for tweets
public_tweets = api.search("trump")
score = []
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")
	score.append(analysis.sentiment)

polarity = 0
subjectivity = 0

for i in range(len(score)):
	polarity = polarity + score[i].polarity
	subjectivity = subjectivity + score[i].subjectivity



print("Average polarity: ", polarity/len(score))
print("Average subjectivity: ", subjectivity/len(score))

#create a labeled tweet dataset in a CSV file