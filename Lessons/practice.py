for number in range(1,4):
    for letter in ["A", "B"]:
        print(number, letter)
print("")

for day in range(1,3):
    for task in range(1,4):
        print("Day", day, "Task", task)


# FINAL CHALLENGE 
numbers = [3, 8, 12, 5, 20, 7]
large_squares = [number ** 2 for number in numbers if number > 10]
print(large_squares)