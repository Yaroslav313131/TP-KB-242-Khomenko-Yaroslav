from sys import argv
from studentlist import StudentList
from utils import Utils

def main():
    if len(argv) < 2:
        print("Error: CSV file name must be provided!")
        return

    file_name = argv[1]
    group_list = StudentList()

    if not Utils.read_from_csv(file_name, group_list):
        print(f"File {file_name} not found. Starting with empty list.")

    while True:
        choice = input("\nAction [C create, U update, D delete, P print, X exit]: ").strip().lower()

        match choice:
            case "c":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                group = input("Group: ")
                group_list.add_student(name, phone, email, group)

            case "u":
                old_name = input("Name to update: ")
                target = group_list.find_by_name(old_name)
                if not target:
                    print("Not found.")
                    continue

                new_name = input(f"New name ({target.name}): ") or target.name
                new_phone = input(f"New phone ({target.phone}): ") or target.phone
                new_email = input(f"New email ({target.email}): ") or target.email
                new_group = input(f"New group ({target.group}): ") or target.group

                group_list.update_student(old_name, new_name, new_phone, new_email, new_group)
                print("Updated.")

            case "d":
                name = input("Name to delete: ")
                if group_list.delete_student(name):
                    print("Deleted.")
                else:
                    print("Not found.")

            case "p":
                print("\n--- Student List ---")
                for s in group_list.get_all():
                    print(s)

            case "x":
                print("Saving...")
                Utils.save_to_csv(file_name, group_list.get_all())
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()