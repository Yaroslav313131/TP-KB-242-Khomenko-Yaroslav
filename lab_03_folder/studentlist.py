from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, name, phone, email, group):
        new_student = Student(name, phone, email, group)
        insert_position = 0
        for item in self.students:
            if name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, new_student)

    def delete_student(self, name):
        for i, student in enumerate(self.students):
            if student.name.lower() == name.lower():
                del self.students[i]
                return True
        return False

    def update_student(self, old_name, new_data):
        for i, student in enumerate(self.students):
            if student.name.lower() == old_name.lower():
                del self.students[i]
                self.add_student(
                    new_data.get("name", student.name),
                    new_data.get("phone", student.phone),
                    new_data.get("email", student.email),
                    new_data.get("group", student.group)
                )
                return True
        return False

    def get_all(self):
        return self.students