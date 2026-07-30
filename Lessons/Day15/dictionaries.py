student = {
    "name": "Peter",
    "age" : 25,
    "school": "IBBUL"
}
student["age"] = 23
student["course"] = "Mathematics"
print(student["name"])
print(student["age"])
print(student["school"])
print(student["course"])
print()

for key in student:
    print(key)

print()

for key in student:
    print(student[key])