#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi_num = sum([int(enron_data[p]['poi']) for p in enron_data.keys()])

print "James Prentice stock value:", enron_data['PRENTICE JAMES']['total_stock_value']

max([enron_data[p]['total_payments'] for p in ['LAY KENNETH L', 'SKILLING JEFFREY K', 'FASTOW ANDREW S']])
[p for p in enron_data.keys() if enron_data[p]['total_payments'] == 103559793]

len(enron_data) - sum([int(enron_data[p]['salary']=='NaN') for p in enron_data.keys()])
len(enron_data) - sum([int(enron_data[p]['email_address']=='NaN') for p in enron_data.keys()])

sum([int(enron_data[p]['total_payments']=='NaN') for p in enron_data.keys()])
sum([int(enron_data[p]['total_payments']=='NaN') for p in enron_data.keys() if enron_data[p]['poi']])/float(len(enron_data))
[int(enron_data[p]['total_payments']) for p in enron_data.keys() if enron_data[p]['poi']]