#Using decision tree submodule of scikiit-learn
from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44], [177,70,43],  [160,60,38],  [154,54,37],
     [166,65,40], [190,90,47],  [175,64,39], [177,70,40 ], [158,55,37],
     [171,75,42], [181,85,43]]
     
Y = ['male', 'female', 'female', 'female', 'male', 'male', 
 	 'male', 'female', 'male', 'female', 'male']

#stores decision tree classifier
clf = tree.DecisionTreeClassifier()

#now have tree variable, can train it on data set
#call the fit method on the classifier variable, which takes 2 arguments
#result stored in updated clf variable
clf = clf.fit(X,Y)

#test it by classifying the gender of someone given a new list of body metrics

prediction = clf.predict([190,70,43])

print prediction