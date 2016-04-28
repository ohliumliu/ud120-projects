#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("/home/yu/MachineLearning/udacity_class_projects/ud120-projects/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

time0 = time()
features_train, features_test, labels_train, labels_test = preprocess()
print "Preprocessing time:", time()-time0, "s"



#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

time0 = time()
clf.fit(features_train, labels_train)
print "Training time:", time()-time0, "s"


# Calculate score. The provided method is
# clf.score(features_test)

time0 = time()
pred = clf.predict(features_test)
print "Prediction time:", time()-time0, "s"
score = numpy.float(sum(pred == labels_test))/len(labels_test)


#########################################################


