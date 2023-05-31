# Write a program that will simulate user scores in a game. Create a list with 5 players’ 
# names after that simulate 100 rounds for each player. As a result of the game create a list
#  with the player's name and score (0-1000 range). And save it to a CSV file. The file should look like this:

# Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345
# ...

import csv
import random

list_ = ["Josh","Luke","Kate","Mark","Mary"]
scorelist =[]

for round in range(100):
    for name in list_:
        score = random.randint(1,1000)
        scorelist.append([name,score])
        

with open("Files2/scorelist.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Score"])    
    for points in scorelist:   
           writer.writerow(points)     