students_data = [
    {"name": "Ihor", "mark": 60},
    {"name": "Michael", "mark": 90},
    {"name": "Zak", "mark": 90},
    {"name": "Anna", "mark": 89},
]

print("Оригінальні дані ")
for student in students_data:
    print(f"Name = {student['name']:<7} Mark = {student['mark']}")


print("Сортування за Оцінкою (зростання)")


sorted_by_mark = sorted(students_data, key=lambda student: student["mark"])

for elem in sorted_by_mark:
    print(f"Name = {elem['name']:<7} Mark = {elem['mark']}")



print("Сортування за Іменем (алфавітний порядок)")


sorted_by_name = sorted(students_data, key=lambda student: student["name"])

for elem in sorted_by_name:
    print(f"Name = {elem['name']:<7} Mark = {elem['mark']}")