def create_student_dict(students):
    return {student[0]: student[1] for student in students}

def calculate_average(student_dict, student_name):
    grades = student_dict.get(student_name, [])
    return sum(grades) / len(grades) if grades else None

def find_highest_average_student(student_dict):
    return max(student_dict, key=lambda student: sum(student_dict[student]) / len(student_dict[student]))

def count_passed_students(student_dict, pass_mark=50):
    return sum(1 for grades in student_dict.values() if sum(grades) / len(grades) >= pass_mark)


students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

student_dict = create_student_dict(students)


print("Dictionary of students and their grades:")
print(student_dict)

print("\nAverage grade for Bob:")
print(calculate_average(student_dict, "Bob"))

print("\nStudent with the highest average grade:")
print(find_highest_average_student(student_dict))

print("\nNumber of students who passed:")
print(count_passed_students(student_dict))
