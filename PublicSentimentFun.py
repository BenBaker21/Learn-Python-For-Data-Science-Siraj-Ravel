import tweepy
from textblob import TextBlob
import os
import csv
import sys, getopt

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
#Open the csv file and make the csv writer
csvF = open('sentiments1.csv', 'a')
csvW = csv.writer(csvF)


#Searching for tweets
averagePolarity = []
averageSubjectivity = []
for x in range(1, len(sys.argv)):
	public_tweets = api.search(sys.argv[x])
	score = []
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		score.append(analysis.sentiment)
		csvW.writerow([tweet.created_at])
		if analysis.sentiment.polarity >= 0 and analysis.sentiment.polarity < .30:
			csvW.writerow("Slightly positive tweet")

		elif analysis.sentiment.polarity > -.30 and analysis.sentiment.polarity < 0:
			csvW.writerow("Slightly negative tweet")

		elif analysis.sentiment.polarity >= .30 and analysis.sentiment.polarity <= 1:
			csvW.writerow("Very positive tweet")

		elif analysis.sentiment.polarity >= -1 and analysis.sentiment.polarity <= -.30:
			csvW.writerow("Very negative tweet")

		if analysis.sentiment.subjectivity >= 0 and analysis.sentiment.subjectivity < .30:
			csvW.writerow("Slight subjectivity")

		elif analysis.sentiment.subjectivity > -.30 and analysis.sentiment.subjectivity < 0:
			csvW.writerow("Slightly negative subjectivity")

		elif analysis.sentiment.subjectivity >= .30 and analysis.sentiment.subjectivity <= 1:
			csvW.writerow("Very subjective")

		elif analysis.sentiment.subjectivity >= -1 and analysis.sentiment.subjectivity <= -.30:
			csvW.writerow("Very negative subjectivity")

		csvW.writerow([analysis])
		csvW.writerow([analysis.sentiment])
		csvW.writerow("")
		#print(tweet.created_at)
		#print(tweet.text) 
		#print(analysis)
		#print (analysis.sentiment)
		#print("")

	polarity = 0
	subjectivity = 0

	for i in range(len(score)):
		polarity = polarity + score[i].polarity
		subjectivity = subjectivity + score[i].subjectivity

	averagePolarity.append(polarity/len(score))
	averageSubjectivity.append(subjectivity/len(score))


csvF.close()

for k in range(len(averagePolarity)):
	print("Search: " + sys.argv[k+1])
	print("Average polarity: ", averagePolarity[k])
	if averagePolarity[k] >= 0 and averagePolarity[k] < .30:
		print("Slightly positive average polarity")

	elif averagePolarity[k] > -.30 and averagePolarity[k] < 0:
		print("Slightly negative average polarity")

	elif averagePolarity[k] >= .30 and averagePolarity[k] <= 1:
		print("Very positive average polarity")

	elif averagePolarity[k] >= -1 and averagePolarity[k] <= -.30:
		print("Very negative average polarity")

	print("Average subjectivity: ", averageSubjectivity[k])
	if averageSubjectivity[k] >= 0 and averageSubjectivity[k] < .30:
		print("Slightly positive average subjectivity")

	elif averageSubjectivity[k] > -.30 and averageSubjectivity[k] < 0:
		print("Slightly negative average subjectivity")

	elif averageSubjectivity[k] >= .30 and averageSubjectivity[k] <= 1:
		print("Very positive average subjectivity")

	elif averageSubjectivity[k] >= -1 and averageSubjectivity[k] <= -.30:
		print("Very negative average subjectivity")

	print("")

#create a labeled tweet dataset in a CSV file