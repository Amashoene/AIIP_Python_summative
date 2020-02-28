# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:54:38 2020

@author: 212560144
"""
#Problem 2.2:

#This code is for dating and time stamping each interval of data collection on the text file.

from datetime import date #This add the date the code was written on the text file.
d1 = date.today() # this dates the file to the day this file was read
print(d1)
file = open ("Sensor_Network_Clusters.txt" , "r") #This code reads the data that is on the textfile.
#write some lines of dataset to the file
for y  in range(1,33): 
    import random 
    float = [random.random() for i in range(1,17)] 
    print('cluster number', y,float) 
    file.readline()
    file.readline()
    file.readline()
    
else: 
    file.close() #close the file when done
    print("finished")  
   

    