file = open("note.txt", "w")
file.write("Python is awesome!")
file.close()

file = open("note.txt", "r")
print(file.read())
file.close()