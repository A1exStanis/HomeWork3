# Write a script that reads the data from the previous CSV file and creates a new file called high_scores.csv 
# where each row contains the player name and their highest score. 
# The final score should be sorted by descending to the highest score. The output CSV file should look like this:

# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

import csv

Mark_list = []
Kate_list = []
Mary_list = []
Luke_list = []
Josh_list = []
highestscore = []
with open("Files2/scorelist.csv", mode="r") as file:
    reader = csv.reader(file)
    list_ = [row for row in reader]
for i in list_:
    if "Mark" in i:
        Mark_list.append(i)
    elif "Kate" in i:
        Kate_list.append(i)
    elif "Mary" in i:
        Mary_list.append(i)
    elif "Luke" in i:
        Luke_list.append(i)
    elif "Josh" in i:
        Josh_list.append(i)
Mark_list.sort()
highestscore.append(Mark_list.pop())
Kate_list.sort()
highestscore.append(Kate_list.pop())
Mary_list.sort()
highestscore.append(Mary_list.pop())
Luke_list.sort()
highestscore.append(Luke_list.pop())
Josh_list.sort()
highestscore.append(Josh_list.pop())
highestscore.sort(reverse=True,key=lambda x: x[1])
with open("Files2/highestscore.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name","Highest score"]) 
    for points in highestscore:   
           writer.writerow(points) 