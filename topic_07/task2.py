class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

students_list = [
    Student("Олена", 22),
    Student("Ганна", 19),
    Student("Ірина", 20),
    Student("Богдан", 22),
    Student("Василь", 25),
    Student("Андрій", 19) 
]
print("--- Несортований список студентів: ---")
for student in students_list:
    print(student)

sorted_students_by_age = sorted(students_list, key=lambda student: student.age)
print("\n--- Список, відсортований за Віком: ---")
for student in sorted_students_by_age:
    print(student)
    
sorted_students_multikey = sorted(students_list, key=lambda student: (student.age, student.name))
print("\n--- Список, відсортований за Віком та Іменем: ---")

for student in sorted_students_multikey:
    print(student)