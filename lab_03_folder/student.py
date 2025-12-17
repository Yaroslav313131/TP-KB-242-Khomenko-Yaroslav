class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return f"Студент: {self.name:15} | Тел: {self.phone:12} | Email: {self.email:20} | Group: {self.group}"

    def to_dict(self):
        return {
            "Studname": self.name,
            "Phone": self.phone,
            "Gmail": self.email,
            "Group": self.group
        }