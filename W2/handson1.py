#students grade management system
students = {}
def add_student(name, grade):
    students[name] = grade
    print(f"Added student: {name} with grade: {grade}")

def calculate_average():
    if students:
        average = sum(students.values()) / len(students)
        return average
    return 0

total = sum(students.values())
print(f"Total of all grades: {total}")
avg = calculate_average() 
print(f"Average grade: {avg}")

add_student("tripan", 85)
add_student("Bob", 90)
add_student("nandi", 78)
add_student("sen", 92)
add_student("Ethan", 88)
calculate_average()

print("Final Students and Grades: ", students)
