# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:25:57 2020

@author: 212560144
"""
#Problem 2.3:
#This code is for ensuring that new data does not overwrite historical data.

from datetime import date 
d1 = date.today() # this dates the file to the day this file was read
print(d1)
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
while True:
    float = [random.random() for i in range(1,17)] 
    #prints floats
    with open ("Sensor_Network_Clusters.txt" , "a") as outfile:
     print('cluster number', y,float)    