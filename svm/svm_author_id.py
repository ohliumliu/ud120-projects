#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

# trim data set to speed things up        
features_train = features_train[:len(features_train)]
labels_train = labels_train[:len(labels_train)]

from sklearn import svm
from sklearn.metrics import accuracy_score
#clf = svm.SVC(kernel='linear')
clf = svm.SVC(C=10000, kernel='rbf')


# training
time0 = time()
clf.fit(features_train, labels_train)
print "Training time is:", time()-time0, "s"

pred = clf.predict(features_test)

score = accuracy_score(labels_test, pred)
print "accuracy is", score

#################################################


