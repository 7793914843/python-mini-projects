import json


class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("\nStudent ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Course     :", self.course)
        print("Marks      :", self.marks)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }


students = []


# Load students from file
def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            for student in data:
                students.append(
                    Student(
                        student["student_id"],
                        student["name"],
                        student["age"],
                        student["course"],
                        student["marks"]
                    )
                )

    except FileNotFoundError:
        students = []


# Save students to file
def save_students():
    data = []

    for student in students:
        data.append(student.to_dict())

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


# Add student
def add_student():
    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    for student in students:
        if student.student_id == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, age, course, marks)

    students.append(student)
    save_students()

    print("Student added successfully!")


# View students
def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        student.display()


# Search student
def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student.student_id == student_id:
            student.display()
            return

    print("Student not found!")


# Update student
def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:

        if student.student_id == student_id:

            print("Enter new details:")

            student.name = input("Enter Name: ")
            student.age = int(input("Enter Age: "))
            student.course = input("Enter Course: ")
            student.marks = float(input("Enter Marks: "))

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found!")


# Delete student
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:

        if student.student_id == student_id:

            students.remove(student)
            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main program
load_students()

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
