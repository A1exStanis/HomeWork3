# Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
# To each file append a random number between 1 and 100. Create a summary file (summary.txt)
# that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
import random

file_name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
summery = open("Files2/summery.txt","a")
for name in file_name:
    with open(f"Files2/{name}.txt","w") as file:
        rand = random.randint(1,100)
        file.write(str(rand))
        summery.write(f"{name}.txt:{rand} \n")
summery.close()