# lab_01.py

# вже відсортований список студентів
students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-242"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "group": "KB-242"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@gmail.com",  "group": "KB-242"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@gmail.com",  "group": "KB-242"}
]

def printAllList():
    for elem in students:
        print(f"Student name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Group: {elem['group']}")
    return


def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    # знаходимо позицію для вставки (щоб залишалось відсортованим)
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("⚠️ Element was not found")
    else:
        del students[deletePosition]
        print("🗑️ Element deleted successfully")
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in students:
        if name == item["name"]:
            updatePosition = students.index(item)
            break
    if updatePosition == -1:
        print("⚠️ Student not found")
        return
    
    print("Leave field empty if you don’t want to change it.")

    # вводимо нові значення
    new_name = input(f"Enter new name ({students[updatePosition]['name']}): ") or students[updatePosition]['name']
    new_phone = input(f"Enter new phone ({students[updatePosition]['phone']}): ") or students[updatePosition]['phone']
    new_email = input(f"Enter new email ({students[updatePosition]['email']}): ") or students[updatePosition]['email']
    new_group = input(f"Enter new group ({students[updatePosition]['group']}): ") or students[updatePosition]['group']

    # оновлюємо дані
    students[updatePosition] = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "group": new_group
    }

    # щоб залишилось відсортовано — видалимо і вставимо знову
    updated_student = students.pop(updatePosition)

    insertPosition = 0
    for item in students:
        if updated_student["name"] > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, updated_student)

    print("✏️ Student info updated successfully")
    return


def main():
    while True:
        choice = input("\nPlease specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match choice:
            case "C" | "c":
                print(" Adding new element:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print(" Updating element:")
                updateElement()
                printAllList()
            case "D" | "d":
                print(" Deleting element:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print(" Printing list:")
                printAllList()
            case "X" | "x":
                print(" Exit()")
                break
            case _:
                print(" Wrong choice, try again.")


if __name__ == "__main__":
    main()