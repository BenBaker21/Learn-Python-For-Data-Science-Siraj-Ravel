import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it
data = fetch_movielens(min_rating=4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
#loss function
#measures the difference between our models prediction and the desired output
#want to minimize it during training, so model gets more accurate
#warp = weighted approximate rank pairwise
#looks at existing user rating pairs and predicts rankings for each, uses gradient descent
model = LightFM(loss='warp')

#can now train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
	#number of users and movies in training data
	n_users, n_items = data['train'].shape

	#generate recommendations for each user we input
	for user_id in user_ids:
		#movies they already like
		#We'll get the list of positive ratings from our data in compressed sparse row format
		#This is a subarray inside the data matrix that we'll retrieve with the indices atribute
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
		#now generate recomendations
		#movies our model predicts they will like
		#a range method of numpy gives us every number from 0 to the number of items 
		#so we can predict the score for every movie
		scores = model.predict(user_id, np.arange(n_items))
		#now sort in order of score
		#Argsort method will return the score indices in descending order thanks to the negative sign
		top_items = data['item_labels'][np.argsort(-scores)]

		#now print out the results
		#first the user id, %s converts user id to a string
		print("User %s" % user_id)
		print("		Known positives:")

		for x in known_positives[:3]:
			print("			%s" % x)

		print("		Recommended: ")

		#prints top 3 recommended
		for x in top_items[:3]:
			print("			%s" % x)

sample_recommendation(model, data, [3, 25, 450])






