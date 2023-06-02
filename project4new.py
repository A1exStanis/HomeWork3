import csv

new_dict ={}
with open("Files2/scorelist.csv", mode="r") as file:
    reader = csv.DictReader(file)
    list_ = [row for row in reader]
list_ = sorted(list_, key=lambda x: x["Score"])

for row in list_:
     new_dict[row["Name"]]={}
     for res in list_:
          new_dict[row["Name"]]=row["Score"]
new_dict = sorted(new_dict.items(), reverse=True, key=lambda x: x[1])

with open("Files2/highestscore.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name","Highest score"])
    for points in new_dict:   
            writer.writerow(points)