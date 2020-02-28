# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:17:45 2020

@author: 212560144
"""
#Problem 1:

y = "cluster number" # y denotes sensor clusters from 1 to 32
for y  in range(1,33): #This returns a list of cluster numbers from 1 to 33 ,exlcuding the upper limit which is 33
    import random # This method is for generating random dataset of floats
    float = [random.random() for i in range(1,17)] #Returns an array of random floats for each cluster number
    print('cluster number', y,float) #prints out range of 16 floats between 0 and 1 for each cluster
else: #Stops the code.
    print("finished")    