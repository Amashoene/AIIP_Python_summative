# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:47:25 2020

@author: 212560144
"""

#Problem 2.1:

#This code is for storing data on a textfile with every iteration of the data set so no data is lost.

#open a file named "Sensor_Network_Clusters" for writing and create it if it does not exist
file = open ("Sensor_Network_Clusters.txt" , "w")
#write some lines of dataset to the file
for y  in range(1,33): 
    file.write("\n")
    import random 
    float = [random.random() for i in range(1,17)] 
    print('cluster number', y,float) 
    file.write("cluster")
    file.write(str(y))
    file.write(str(float))
else: 
    file.close() #close the file when done
    print("finished")  
    