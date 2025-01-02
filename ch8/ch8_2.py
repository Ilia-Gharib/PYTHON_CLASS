import json
import os

STUDENT_FILE = "students.json"

def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, "r") as file:
        return json.load(file)

def save_students(data):
    with open(STUDENT_FILE, "w") as file:
        json.dump(data, file, indent=4)

def display_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")

def edit_student(student_id):
    students = load_students()
    for student in students:
        if student['id'] == student_id:
            print(f"Current Record: {student}")
            student['name'] = input("Enter new name: ")
            student['grade'] = input("Enter new grade: ")
            save_students(students)
            print("Student record updated.")
            return
    print("Student not found.")

def add_student():
    students = load_students()
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    students.append({"id": student_id, "name": name, "grade": grade})
    save_students(students)
    print("Student added successfully.")

def main():
    while True:
        print("\n1. Display all students")
        print("2. Edit a student record")
        print("3. Add a new student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_students()
        elif choice == "2":
            student_id = input("Enter Student ID to edit: ")
            edit_student(student_id)
        elif choice == "3":
            add_student()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
