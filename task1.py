import random 

ourList = list()
belowFive = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    if ourList[count-1] < 5:
        belowFive.append(ourList[count-1])
    
print(ourList)
print(belowFive)
