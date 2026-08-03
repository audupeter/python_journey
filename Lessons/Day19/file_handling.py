file = open("notes.txt", "w")
file.write("Hello, Peter")
file.close()

file = open("notes.txt", "a")
file.write("\nWelcome back")
file.close()

file = open("notes.txt", "r")
print(file.read())
file.close()