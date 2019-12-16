from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

#[height, weight, shoe size]
X = [[181,80,44], [177,70,43],  [160,60,38],  [154,54,37],
     [166,65,40], [190,90,47],  [175,64,39], [177,70,40 ], [158,55,37],
     [171,75,42], [181,85,43]]
     
Y = ['male', 'female', 'female', 'female', 'male', 'male', 
 	 'male', 'female', 'male', 'female', 'male']

classifiers = [DecisionTreeClassifier(), KNeighborsClassifier(n_neighbors = 5), LogisticRegression(), 
			   SGDClassifier(loss = 'modified_huber', shuffle=True, random_state=101), Perceptron(),
 			   SVC(kernel="linear", C=0.025, random_state=101), 
 			   RandomForestClassifier(n_estimators=70, oob_score=True, n_jobs=-1, random_state=101, max_features=None, min_samples_leaf=30),
 			   GaussianNB()]
names = ['DecisionTreeClassifier', 'KNeighborsClassifier', 'LogisticRegression', 'SGDClassifier', 'Perceptron',
 		'SVC', 'RandomForestClassifier', 'GaussianNB']
#variable to store the index of the best one
j = 0;
best = 0;
for i in range(len(names)):
	clf = classifiers[i]
	clf.fit(X,Y)
	score = clf.score(X,Y)
	print("Algorithm: ", names[i], " --> Score: ", score)
	if(best <= score):
		j = i
		best = score;
	
print("Best classifier: ", names[j])
clf = classifiers[j]
print(clf.predict([[190, 70, 43]]))