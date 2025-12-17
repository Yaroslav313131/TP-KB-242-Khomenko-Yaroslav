import csv
from student import Student

class Utils:
    @staticmethod
    def read_from_csv(file_path, student_list_obj):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list_obj.add_student(
                        row["Studname"], row["Phone"], row["Gmail"], row["Group"]
                    )
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def save_to_csv(file_path, students_data):
        fieldnames = ["Studname", "Phone", "Gmail", "Group"]
        with open(file_path, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for s in students_data:
                writer.writerow({
                    "Studname": s.name, "Phone": s.phone,
                    "Gmail": s.email, "Group": s.group
                })