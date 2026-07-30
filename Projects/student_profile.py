student = {
    "name": "Alex",
    "age": 24,
    "deparment": "Computer Science",
    "level": 200
}

for key in student:
    print(student[key])

print()

student["level"] = 300

for key in student:
    print(student[key])