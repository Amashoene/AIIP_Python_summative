#Problem 3 
#This code creates a Corrupted dataset containing at least one entry where the value is "err"

y = "cluster number" 
for y  in range(1,33):
    import random
    float = [random.random() for i in range(1,17)]
    float [5] = 'err'
    print('cluster number', y,float)
    
else:
    print("finished")    

count = 0 #This code checks where the error is within the dataset
for i in range(1,17):
 if (i == "0"):
  count += 'err'
 print(count, "error found")
