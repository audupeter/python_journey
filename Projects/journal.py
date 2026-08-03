file = open("journal.txt", "w")
file.write("Day 19: I learnt file handling in python.")
file.close()

# stretch challenge
file = open("journal.txt", "a")
file.write("\nHow to open, write, read and close files in python.")
file.close()

file = open("journal.txt", "r")
print(file.read())
file.close()

# stretch challenge

file = open("journal.txt", "a")
file.write("\nHow to open, write, read and close files in python.")
file.close()
