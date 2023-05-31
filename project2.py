# Create a file with some content. As example, you can take this one:

# “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
# labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
# laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
# voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
# proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.

# Create a second file and copy the content of the first file to the second file in upper case.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut \nlabore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco \nlaboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in \nvoluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non \nproident, sunt in culpa qui officia deserunt mollit anim id est laborum"
with open("Files2/text1.txt", "w") as file:
    file.write(text)
with open("Files2/text1.txt", "r") as file:    
    text = file.read()
with open("Files2/text2.txt", "w") as file:
    for line in text:
        line = line.upper()
        file.write(line)