# Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
# To each file append a random number between 1 and 100. Create a summary file (summary.txt)
# that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
import random

ord = 65
for x in range(26):
    x += ord
    name = chr(x)
    rand = random.randint(1,100)
    with open(f"Files2/{name}.txt","w") as file:
        file.write(str(rand))
    with open("Files2/summery.txt","a") as file:
        file.write(f"{name}.txt:{rand} \n")