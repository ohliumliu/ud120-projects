#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    error = (predictions - net_worths)**2
    #uncleaned_data = np.array(zip(ages.ravel(), net_worths.ravel(), error.ravel()))
    uncleaned_data = np.array([[ages[i][0], net_worths[i][0], error[i][0]] for i in range(0, len(ages))])
    sorted_data = uncleaned_data[uncleaned_data[:,2].argsort()]
    cleaned_data_array = sorted_data[0:len(error)-len(error)/10]
    cleaned_data = [(cleaned_data_array[i][0], cleaned_data_array[i][1], cleaned_data_array[i][2]) for i in range(0, len(cleaned_data_array[:,0]))]
    ### your code goes here    
    return cleaned_data

