print("=" * 40)
print("Student Management System")
print("Created by Ali Moradi")
print("=" * 40)

student_list = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.\n")
        return

    age = input("Enter student age: ").strip()
    major = input("Enter student major: ").strip()

    student = {
        "name": name,
        "age": age,
        "major": major
    }

    student_list.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(student_list) == 0:
        print("No students found.\n")
        return

    print(f"\nTotal Students: {len(student_list)}")
    print("-" * 50)

    for i, student in enumerate(student_list, start=1):
        print(
            f"{i}. {student['name']} | "
            f"Age: {student['age']} | "
            f"Major: {student['major']}"
        )

    print()


def search_student():
    keyword = input("Enter student name to search: ").strip()

    found = False

    for student in student_list:
        if keyword.lower() in student["name"].lower():
            print(
                f"Found: {student['name']} | "
                f"Age: {student['age']} | "
                f"Major: {student['major']}"
            )
            found = True

    if not found:
        print("Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ").strip()

    for student in student_list:
        if student["name"].lower() == name.lower():
            student_list.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def save_students():
    try:
        with open("students.txt", "w", encoding="utf-8") as file:
            for student in student_list:
                file.write(
                    f"{student['name']},"
                    f"{student['age']},"
                    f"{student['major']}\n"
                )

        print("Data saved successfully!\n")

    except Exception as e:
        print("Error saving file:", e)


def load_students():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    name, age, major = line.split(",")

                    student_list.append({
                        "name": name,
                        "age": age,
                        "major": major
                    })

                except ValueError:
                    print("Skipping invalid record.")

    except FileNotFoundError:
        pass


def menu():
    load_students()

    while True:
        print("===== MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            save_students()

        elif choice == "6":
            save_students()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


menu()
