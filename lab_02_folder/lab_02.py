import csv
from sys import argv


def add_student(student_list, name, phone, email, group):
    new_item = {"name": name, "phone": phone, "email": email, "group": group}
    insert_position = 0
    for item in student_list:
        if name > item["name"]:
            insert_position += 1
        else:
            break
    student_list.insert(insert_position, new_item)

def delete_student(student_list, name):
    for i, item in enumerate(student_list):
        if item["name"].lower() == name.lower():
            del student_list[i]
            return True
    return False

def update_student(student_list, old_name, new_data):
    for i, item in enumerate(student_list):
        if item["name"].lower() == old_name.lower():
            del student_list[i]
            

            add_student(
                student_list,
                new_data.get("name", item["name"]),
                new_data.get("phone", item["phone"]),
                new_data.get("email", item["email"]),
                new_data.get("group", item["group"])
            )
            return True
    return False

def read_data_from_file(student_list, input_file):

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                add_student(
                    student_list,
                    row["Studname"],
                    row["Phone"],
                    row["Gmail"],
                    row["Group"]
                )
        return True
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено: {input_file}")
        return False
    except KeyError as e:
        print(f"Помилка: Відсутній очікуваний стовпець у CSV: {e}")
        return False

def save_data_to_file(student_list, output_file):
    fieldnames = ["Studname", "Phone", "Gmail", "Group"]
    try:
        with open(output_file, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in student_list:
                writer.writerow({
                    "Studname": row["name"],
                    "Phone": row["phone"],
                    "Gmail": row["email"],
                    "Group": row["group"]
                })
        return True
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")
        return False


def print_all_list(student_list):
    if not student_list:
        print("Список студентів порожній.")
        return
    print("\n--- Довідник студентів ---")
    print(f"{'Ім\'я':<10} {'Телефон':<15} {'Email':<25} {'Група'}")
    print("=" * 60)
    for elem in student_list:
        print(
            f"{elem['name']:<10} {elem['phone']:<15} {elem['email']:<25} {elem['group']}"
        )
    print("--------------------------\n")

def add_new_element_interactive(student_list):
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть Email студента: ")
    group = input("Введіть групу студента: ")
    
    add_student(student_list, name, phone, email, group)
    print("Новий елемент успішно додано.")

def delete_element_interactive(student_list):
    name_to_delete = input("Введіть ім'я студента для видалення: ")
    if delete_student(student_list, name_to_delete):
        print(f"Студента '{name_to_delete}' було видалено.")
    else:
        print(f"Помилка: Студента '{name_to_delete}' не знайдено.")

def update_element_interactive(student_list):
    old_name = input("Введіть ім'я студента, дані якого потрібно оновити: ")
    
    found_student = None
    for item in student_list:
        if item["name"].lower() == old_name.lower():
            found_student = item
            break
            
    if found_student:
        print(f"Оновлення даних для: {found_student['name']} (Група: {found_student['group']})")
        
        new_name = input(f"Введіть нове ім'я (поточне: {found_student['name']}): ") or found_student['name']
        new_phone = input(f"Введіть новий телефон (поточний: {found_student['phone']}): ") or found_student['phone']
        new_email = input(f"Введіть новий email (поточний: {found_student['email']}): ") or found_student['email']
        new_group = input(f"Введіть нову групу (поточна: {found_student['group']}): ") or found_student['group']

        new_data = {
            "name": new_name, 
            "phone": new_phone, 
            "email": new_email, 
            "group": new_group
        }
        
        if update_student(student_list, old_name, new_data):
             print("Елемент успішно оновлено.")
        else:
            print("Виникла внутрішня помилка при оновленні.")
            
    else:
        print(f"Помилка: Студента '{old_name}' не знайдено.")


def main():
    student_list = []

    if len(argv) < 2:
        print("Використання: python lab_02.py lab_02.csv")
        return

    input_output_file = argv[1]

    print(f"Завантаження даних з {input_output_file}...")
    if read_data_from_file(student_list, input_output_file):
        print(f"Завантажено {len(student_list)} студентів.")
    else:
        print("Початок роботи з порожнім списком. Дані будуть збережені у вказаний файл при виході.")

    while True:
        choice = input(
            "\nВиберіть дію [ C створити, U оновити, D видалити, P друк, X вихід ]: "
        ).upper()

        match choice:
            case "C":
                add_new_element_interactive(student_list)
            case "U":
                update_element_interactive(student_list)
            case "D":
                delete_element_interactive(student_list)
            case "P":
                print_all_list(student_list)
            case "X":
                print("\nЗбереження даних та вихід...")
                save_data_to_file(student_list, input_output_file)
                print("Дані успішно збережено. До побачення.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()